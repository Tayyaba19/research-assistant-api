import time

class ResearchHandler:
    def __init__(self, topic: str, response_format: str, client, task):
        self.topic = topic
        self.response_format = response_format
        self.client = client
        self.task = task

    def generate_response(self) -> str:
        try:
            execution = self.client.executions.create(
                task_id=self.task.id,
                input={
                    "topic": self.topic,
                    "response_format": self.response_format
                }
            )

            while (result := self.client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
                print(f"Status: {result.status}")
                time.sleep(1)

            if result.status == "succeeded":
                return result.output['search_results']['choices'][0]['message']['content']
            else:
                print(f"Execution failed: {result.error}")
                return "Sorry, unable to process your request."

        except Exception as e:
            print(f"Error while processing task: {e}")
            return "An error occurred while processing your request."
