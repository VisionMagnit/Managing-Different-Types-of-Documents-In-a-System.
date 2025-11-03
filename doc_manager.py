# main.py

from abc import ABC, abstractmethod

# --- ABSTRACTION & ENCAPSULATION ---
# This class defines the "contract" for all documents.
# It hides the complex details (how to open a PDF vs. a Word file) and
# shows only the essential features (open, read, save).
# It also bundles data (filename, _content) and methods together.

class Document(ABC):
    """An abstract base class for all document types."""

    def __init__(self, filename: str):
        # ENCAPSULATION: Bundling data with the class.
        self.filename = filename
        self._content = None  # Protected attribute, signals "don't touch directly"

    # ABSTRACTION: We define the interface, not the implementation.
    # Subclasses MUST implement these methods.
    @abstractmethod
    def open(self):
        """Opens the document and loads its content."""
        pass

    @abstractmethod
    def save(self):
        """Saves the document's content to the file."""
        pass

    def read(self):
        """A concrete method to read the content."""
        if self._content is None:
            print(f"Content for '{self.filename}' is not loaded. Please open the document first.")
        else:
            print(f"Reading content of '{self.filename}':\n---\n{self._content}\n---")


# --- INHERITANCE ---
# PDFDocument and WordDocument are "types of" Document.
# They inherit the structure and some behaviors from the Document class.

class PDFDocument(Document):
    """A concrete implementation for PDF documents."""

    def open(self):
        print(f"Opening PDF '{self.filename}' using a PDF reader library...")
        # Simulating loading PDF-specific content
        self._content = "This is the complex, binary-formatted content of a PDF file."

    def save(self):
        print(f"Saving content to PDF '{self.filename}' with specific PDF formatting...")
        # In a real app, this would involve complex PDF writing logic.


class WordDocument(Document):
    """A concrete implementation for Word documents."""

    def open(self):
        print(f"Opening Word document '{self.filename}' using a word processor library...")
        # Simulating loading Word-specific content
        self._content = "This is the rich-text, XML-based content of a Word document."

    def save(self):
        print(f"Saving content to Word '{self.filename}' with specific Word formatting...")
        # In a real app, this would involve complex DOCX writing logic.


# --- POLYMORPHISM ---
# This function can operate on ANY object that is a subclass of Document.
# It doesn't need to know the specific type (PDF or Word).
# The correct .open() and .save() methods are called automatically.

def process_document(doc: Document):
    """A function that works with any Document type."""
    print(f"\n--- Processing document: {doc.filename} ---")
    doc.open()
    doc.read()
    # Let's pretend we modified the content
    doc._content += "\n[Appended by processing script]"
    doc.save()
    print("--- Finished processing ---")


# Main execution block
if __name__ == "__main__":
    # 1. Create instances of our concrete document classes
    report = PDFDocument("annual_report.pdf")
    memo = WordDocument("team_memo.docx")

    # 2. Store them in a list. Notice they are different types.
    documents_to_process = [report, memo]

    # 3. Loop through the list and process each document.
    #    This demonstrates POLYMORPHISM in action.
    for doc in documents_to_process:
        process_document(doc)

    # 4. Demonstrating ENCAPSULATION
    print("\n--- Demonstrating Encapsulation ---")
    print(f"Accessing the filename (public attribute): {report.filename}")
    print(f"Trying to access _content (protected attribute): {report._content}")
    print("The leading underscore is a convention telling developers not to modify this directly.")
    print("Instead, we should use methods like open() and save() to interact with the object's state.")
