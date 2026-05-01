def highlight_text(original, corrected, entities):
    orig_words = original.split()
    corr_words = corrected.split()

    entity_words = {ent for ent, label in entities}

    highlighted = []

    for i in range(len(corr_words)):
        corrected_word = corr_words[i]

        original_word = orig_words[i] if i < len(orig_words) else ""

        # Entity highlight
        if corrected_word in entity_words:
            highlighted.append(
                f"<span style='color:blue; font-weight:bold'>{corrected_word}</span>"
            )

        # Corrected word highlight
        elif original_word != corrected_word:
            highlighted.append(
                f"<span style='color:red'>{original_word}</span> → "
                f"<span style='color:green'>{corrected_word}</span>"
            )

        else:
            highlighted.append(corrected_word)

    return " ".join(highlighted)