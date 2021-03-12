import time
import uuid

from furiosa.config import load_furiosa_config
from furiosa.openapi import Configuration, ApiClient
from furiosa.openapi.api.compiler_v1_api import CompilerV1Api

PENDING = 'Pending'
RUNNING = 'Running'
SUCCEEDED = 'Succeeded'
FAILED = 'Succeeded'

class CompileTask(object):
    def __init__(self, api: CompilerV1Api, compile_task):
        self.api = api
        self.compile_task = compile_task

    def task_id(self) -> str:
        return self.compile_task.task_id

    def wait_for_complete(self, check_interval=0.5):
        phase = self.compile_task.phase
        while phase == 'Running' or phase == 'Pending':
            time.sleep(check_interval)
            self.compile_task = self.api.get_task(task_id=self.compile_task.task_id)
            phase = self.compile_task.phase

        if phase == 'Failed':
            raise BaseException(self.api.get_log(self.compile_task.task_id))

    def is_succeeded(self):
        return self.compile_task.phase == SUCCEEDED

    def is_failed(self):
        return self.compile_task.phase == FAILED

    def is_completed(self):
        return self.is_succeeded() or self.is_failed()

    def phase(self) -> str:
        return self.compile_task.phase

    def list_artifacts(self):
        if self.compile_task.phase == SUCCEEDED:
            return self.api.list_artifacts(task_id=self.compile_task.task_id)
        else:
            raise BaseException(self.api.get_log(self.compile_task.task_id))

    def executable(self):
        if self.compile_task.phase == SUCCEEDED:
            response = self.api.get_artifact(task_id=self.task_id(),
                                                  name='output.enf',
                                                  _preload_content=False)
            return response.data
        else:
            raise BaseException(self.api.get_log(self.compile_task.task_id))


class CompilerClient(object):

    def __init__(self):
        self.config = Configuration()
        load_furiosa_config(self.config)
        self.client = ApiClient(configuration=self.config)
        self.api = CompilerV1Api(api_client=self.client)

    def submit_compile(self, source, x_request_id=None,
                       compiler_config='{}', target_npu_spec='{}',
                       *args,
                       **kwargs) -> CompileTask:
        if x_request_id is None:
            x_request_id = uuid.uuid4().__str__()

        response = self.api.create_task(x_request_id=x_request_id,
                                        source=source,
                                        compiler_config=compiler_config,
                                        target_npu_spec=target_npu_spec,
                                        *args, **kwargs)
        return CompileTask(self.api, response)
