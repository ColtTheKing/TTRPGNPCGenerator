import aspose.words as aw

def edit_pdf():
    doc = aw.Document("base_vampire_char_sheet.pdf")
    builder = aw.DocumentBuilder(doc)

    # Insert text at the beginning of the document.
    builder.move_to_document_start()
    builder.writeln("Morbi enim nunc faucibus a.")
    builder.move_to_document_end()
    doc.update_page_layout()
    
    doc.save("output_chars/character.pdf")