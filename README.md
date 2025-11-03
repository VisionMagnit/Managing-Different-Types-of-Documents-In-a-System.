Of course! Let's demonstrate the four pillars of Object-Oriented Programming (OOP) in Python by solving a practical problem: managing different types of documents in a system.

Our goal is to create a system that can handle various document types (like PDFs and Word documents), allowing us to open, read, and save them through a common interface, even though their internal workings are different.

The Four Pillars of OOP
Encapsulation: Bundling data (attributes) and methods that operate on the data into a single unit (a class). It also involves restricting direct access to some of an object's components, which is known as data hiding.
Abstraction: Hiding complex implementation details and showing only the essential features of the object. It's about defining a simple interface that the outside world can use.
Inheritance: A mechanism where a new class (subclass/child) derives properties and behaviors from an existing class (superclass/parent). This promotes code reuse.
Polymorphism: The ability of an object to take on many forms. In practice, it means we can treat objects of different classes that share a common interface in the same way.
The Problem: A Document Management System
We need to represent different document types. Each document has a filename and content. However, the way we "open" and "save" a PDF is fundamentally different from a Word document. We want our main application code to be simple and not worry about these differences.

The Solution: Implementing with the Four Pillars
Let's build the solution step-by-step, highlighting each pillar.

1. Abstraction & Encapsulation: The Blueprint
First, we define a "blueprint" for what any document should be able to do. We don't care how it does it yet, just what it does. This is Abstraction. We'll use Python's abc (Abstract Base Class) module to enforce this.

We'll also bundle the data (filename, _content) and methods (open, read, save) together in a class. This is Encapsulation. We'll use a leading underscore (_content) to signal that this attribute is for internal use and shouldn't be modified directly from outside the class.
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

            
           2. Inheritance: Creating Specific Document Types
Now, we create concrete classes for PDFDocument and WordDocument. They will inherit from our Document blueprint. This means they automatically get the __init__ and read methods. They only need to provide the specific implementation for the abstract open
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

        3. Polymorphism: Treating All Documents the Same
        This is where the magic happens. Because both PDFDocument and WordDocument follow the same Document interface, we can write a single function that can operate on any type of document, without knowing or caring if it's a PDF or a Word file.

When we call doc.open(), Python automatically figures out at runtime which open method to use—the one from PDFDocument or the one from WordDocument. This is Polymorphism.
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

    Putting It All Together: The Main Program
Now let's run our system and see all four pillars in action.

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

    Expected Output
    --- Processing document: annual_report.pdf ---
Opening PDF 'annual_report.pdf' using a PDF reader library...
Reading content of 'annual_report.pdf':
---
This is the complex, binary-formatted content of a PDF file.
---
Saving content to PDF 'annual_report.pdf' with specific PDF formatting...
--- Finished processing ---

--- Processing document: team_memo.docx ---
Opening Word document 'team_memo.docx' using a word processor library...
Reading content of 'team_memo.docx':
---
This is the rich-text, XML-based content of a Word document.
---
Saving content to Word 'team_memo.docx' with specific Word formatting...
--- Finished processing ---

--- Demonstrating Encapsulation ---
Accessing the filename (public attribute): annual_report.pdf
Trying to access _content (protected attribute): This is the complex, binary-formatted content of a PDF file.

[Appended by processing script]
The leading underscore is a convention telling developers not to modify this directly.
Instead, we should use methods like open() and save() to interact with the object's state.

Summary of How the Pillars Solved the Problem
Abstraction gave us a simple Document interface, hiding the messy details of file formats from our main application logic.
Encapsulation kept the document's data (_content) and its operations (open, save) together, protecting the data from accidental corruption.
Inheritance allowed us to create PDFDocument and WordDocument classes that reused code from the Document base class, making our system DRY (Don't Repeat Yourself).
Polymorphism was the key to flexibility. It let our process_document function handle a list of mixed document types seamlessly, making our code clean, scalable, and easy to extend with new document types (e.g., TextDocument, ExcelSheet) in the future.

    
