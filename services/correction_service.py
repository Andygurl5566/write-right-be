# Find the occurrence of a substring in a string.
# Used to find the start index of each mistake in the original text.
def find_occurrence(text, substring, start_position=0):
    return text.find(substring, start_position)


# Add start/end indices to each mistake for frontend highlighting.
def add_indices(original_text, analysis):

    last_index = 0

    for mistake in analysis["mistakes"]:

        start = find_occurrence(
            original_text,
            mistake["original"],
            last_index
        )

        if start != -1:
            mistake["start"] = start
            mistake["end"] = start + len(mistake["original"])

            last_index = mistake["end"]

        else:
            mistake["start"] = None
            mistake["end"] = None

    return analysis