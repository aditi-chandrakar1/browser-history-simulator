"""
Browser History Simulator
-------------------------
DSA Concept : Stack (LIFO - Last In, First Out)
Language    : Python 3

Problem Statement:
    Simulate how a web browser handles the Back and Forward buttons.

How it works:
    - back_stack    : pages we can go BACK to
    - forward_stack : pages we can go FORWARD to
    - current       : the page we are on right now

    Visit new page : push current -> back_stack, set new page, clear forward_stack
    Back           : push current -> forward_stack, pop back_stack -> current
    Forward        : push current -> back_stack, pop forward_stack -> current

Time Complexity : O(1) for visit, back and forward (push/pop on a stack)
Space Complexity: O(n) where n = number of pages visited
"""


# ---------------------------------------------------------------
# Our own Stack class (built from scratch using a Python list)
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item on top of the stack. O(1)"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item. O(1)"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Look at the top item without removing it. O(1)"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


# ---------------------------------------------------------------
# Browser class that uses two stacks
# ---------------------------------------------------------------
class Browser:
    def __init__(self, home_page="home"):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = home_page

    def visit(self, url):
        """Open a new page."""
        self.back_stack.push(self.current)
        self.current = url
        # A new visit erases the forward history (just like a real browser)
        self.forward_stack.clear()
        print(f"Visited: {self.current}")

    def back(self):
        """Go to the previous page."""
        if self.back_stack.is_empty():
            print("Cannot go back - no previous page.")
            return
        self.forward_stack.push(self.current)
        self.current = self.back_stack.pop()
        print(f"Went back to: {self.current}")

    def forward(self):
        """Go to the next page."""
        if self.forward_stack.is_empty():
            print("Cannot go forward - no next page.")
            return
        self.back_stack.push(self.current)
        self.current = self.forward_stack.pop()
        print(f"Went forward to: {self.current}")

    def show_history(self):
        """Display the back stack, current page and forward stack."""
        print("\n----- Browser State -----")
        print("Back pages   :", self.back_stack.items if not self.back_stack.is_empty() else "(empty)")
        print("Current page :", self.current)
        # Show forward pages in the order they would be visited
        forward_pages = self.forward_stack.items[::-1]
        print("Forward pages:", forward_pages if forward_pages else "(empty)")
        print("-------------------------\n")


# ---------------------------------------------------------------
# Menu-driven program
# ---------------------------------------------------------------
def main():
    browser = Browser("home")
    print("=== Browser History Simulator ===")
    print(f"You are on: {browser.current}")

    while True:
        print("\n1. Visit a new page")
        print("2. Back")
        print("3. Forward")
        print("4. Show history")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            url = input("Enter page name / URL: ").strip()
            if url == "":
                print("Page name cannot be empty.")
            else:
                browser.visit(url)
        elif choice == "2":
            browser.back()
        elif choice == "3":
            browser.forward()
        elif choice == "4":
            browser.show_history()
        elif choice == "5":
            print("Thank you for using the simulator. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
