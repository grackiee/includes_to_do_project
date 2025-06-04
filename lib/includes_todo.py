def includes_todo(note_line):
    if "#TODO" in note_line:
        return True
    else:
        return False