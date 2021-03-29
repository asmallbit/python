class AnonymousSurney():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(question):
        print(question)

    def save_reponds(self, new_respond):
        self.responses.append(new_respond)

    def show_result(self):
        print("Survey results:")
        for response in responses:
            print('- '+response)

