from document import Document

# Creating a document containing a list of two lists
ORIGINAL_DOCUMENT = Document("Original", [[1, 2, 3, 4], [5, 6, 7, 8]])
print(ORIGINAL_DOCUMENT)
print()

# Clone 1
DOCUMENT_COPY_1 = ORIGINAL_DOCUMENT.clone(mode=1)
DOCUMENT_COPY_1.name = "Copy 1"
DOCUMENT_COPY_1.arr[1][2] = 200
print("DOCUMENT_COPY_1")
print(DOCUMENT_COPY_1)
print("ORIGINAL_DOCUMENT")
print(ORIGINAL_DOCUMENT)
print()

# Clone 2
DOCUMENT_COPY_2 = ORIGINAL_DOCUMENT.clone(mode=2)
DOCUMENT_COPY_2.name = "Copy 2"
# DOCUMENT_COPY_2.arr[1] = [9, 10, 11, 12]
DOCUMENT_COPY_2.arr[1][0] = 12
print("DOCUMENT_COPY_2")
print(DOCUMENT_COPY_2)
DOCUMENT_COPY_2.arr[1] = [9, 10, 11, 12]
print(DOCUMENT_COPY_2)
print("ORIGINAL_DOCUMENT")
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_3 = ORIGINAL_DOCUMENT.clone(3)  # deep copy (recursive)
DOCUMENT_COPY_3.name = "Copy 3"
# This does NOT modify ORIGINAL_DOCUMENT because it
# deep copies all levels recursively when using mode 3
DOCUMENT_COPY_3.arr[1][0] = "5678"
print("DOCUMENT_COPY_3")
print(DOCUMENT_COPY_3)
print("ORIGINAL_DOCUMENT")
print(ORIGINAL_DOCUMENT)
print()
