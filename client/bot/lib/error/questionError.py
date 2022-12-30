import question_ui as qui

def isApplySolution(handler:function):
    if qui.confirm("Do you want to applied the suggested solution"):
        handler()
    