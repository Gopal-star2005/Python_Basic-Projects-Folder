"""
Word Counter
A program that reads a text file and counts the number of words
"""

import os

def count_words(file_path):
    """
    Reads a file and counts the number of words
    
    Args:
        file_path: Path to the text file
        
    Returns:
        Number of words in the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Split content into words
            words = content.split()
            
            # Count words
            word_count = len(words)
            
            return word_count, content
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found!")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to read '{file_path}'!")
    except Exception as e:
        raise Exception(f"Error: An unexpected error occurred: {str(e)}")

def create_sample_file(file_name):
    """Creates a sample text file for testing"""
    sample_text = """Python is a high-level, interpreted programming language.
It is known for its simplicity and readability.
Python is widely used in web development, data science, artificial intelligence, and automation.
The language was created by Guido van Rossum and first released in 1991.
Python's design philosophy emphasizes code readability with significant use of whitespace."""
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(sample_text)
    
    print(f"Sample file '{file_name}' created successfully!")

def display_statistics(file_path, word_count, content):
    """Displays detailed statistics about the file"""
    print("\n" + "=" * 50)
    print("WORD COUNT RESULTS")
    print("=" * 50)
    print(f"File: {file_path}")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {len(content)}")
    print(f"Total Characters (excluding spaces): {len(content.replace(' ', ''))}")
    print(f"Total Lines: {len(content.split(chr(10)))}")
    print("=" * 50)

def main():
    """Main function"""
    print("=" * 50)
    print("WORD COUNTER PROGRAM")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Count words in an existing file")
        print("2. Create a sample file and count words")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
        
        elif choice == '2':
            file_name = input("Enter name for sample file (e.g., sample.txt): ")
            if not file_name.endswith('.txt'):
                file_name += '.txt'
            
            create_sample_file(file_name)
            
            try:
                word_count, content = count_words(file_name)
                display_statistics(file_name, word_count, content)
            except Exception as e:
                print(f"\n{e}")
        
        elif choice == '1':
            file_path = input("Enter the file path: ")
            
            try:
                word_count, content = count_words(file_path)
                display_statistics(file_path, word_count, content)
                
                # Display first few words as preview
                words = content.split()
                if words:
                    preview = ' '.join(words[:20])
                    print(f"\nPreview (first 20 words):\n{preview}...")
            
            except Exception as e:
                print(f"\n{e}")
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
