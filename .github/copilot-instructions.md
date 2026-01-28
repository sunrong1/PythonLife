# PythonLife - AI Copilot Instructions

## Project Overview
**PythonLife** is a comprehensive Python algorithm practice repository focused on LeetCode problem solutions and Python fundamentals. It serves as a learning record for algorithm mastery through iterative practice and refinement.

- **Python Version**: 3.8+
- **IDE**: PyCharm
- **Primary Focus**: Algorithm solutions with multiple implementation approaches and iterations

## Repository Structure

### `/leetcode-life/` - Algorithm Solutions
Organized by algorithm categories and problem difficulty:
- **array/** - Array manipulation problems
- **linkedlist/** - Linked list operations (with `myLinkedList.py` containing base `ListNode` class)
- **DP/** - Dynamic programming solutions (01-knapsack pattern, optimization)
- **back-track/** - Backtracking algorithms (tree exploration, constraint satisfaction)
- **BFS/** - Graph/tree traversal (flood fill, shortest path)
- **find/** - Binary search and two-pointer techniques
- **heap/** - Heap data structure operations
- **sort/** - Sorting algorithms
- **math/** - Bitwise operations, number manipulation
- **recursion/** - Recursive problem solutions
- **number/** - Number theory problems
- **tree/** - Tree traversal and manipulation

### `/python-basic/` - Core Concepts
Educational files demonstrating Python fundamentals (types, functions, data structures).

### `/doc/` - Developer Guides
- `Leetcode-best-way.md` - Problem-solving methodology and data structure techniques
- `pycharm-best-practice.md` - PyCharm workflow guidance

### `/image-life/` - Image Processing
Separate module for image manipulation problems (see `findwavemax.py`).

## Naming Conventions

**Problem Files**: `NO_{problem_id}_{short_name}_{difficulty}.py`
- Examples: `NO_1_two_sum_easy.py`, `NO_22_generate-parentheses_medium.py`
- Difficulty levels: `easy`, `medium`, `hard`

**Classes**: 
- Solution wrappers: `class Solution():` (note: missing type hints in base pattern)
- Data structures: `class ListNode:`, `class TreeNode:` (using `x` or `val` for value)

## Key Patterns & Conventions

### Solution Structure
```python
class Solution():
    def methodName(self, param1, param2) -> ReturnType:
        """
        Chinese method description with docstring
        :type param: Description
        :rtype: ReturnType
        """
        # Implementation
```

### Multiple Solutions Pattern
Files often contain multiple implementations (e.g., `twoSum`, `twoSum2`) demonstrating:
1. Initial approach
2. Optimized approach
3. Alternative algorithms
Label solutions with comments showing iteration/optimization level.

### Linked List Base Class
Use `ListNode` from `myLinkedList.py`:
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```
Include `node_print()` method for debugging.

### Backtracking Template Pattern
- Use inner recursive function `track()` or `dfs()`
- Maintain state list, modify before recursion, restore after
- Clearly separate "go forward" (append) and "go back" (pop) phases
- Document recursion stopping conditions and design logic

### Dynamic Programming Pattern
- Use list initialization: `dp = [0] * (n + 1)`
- Explicitly set boundary conditions (index 0, 1)
- Loop from index 2 onwards to build solution

## Critical Developer Notes

### Learning Methodology
The repository follows a progression model documented in README:
- **第一次练习** (1st attempt): Initial solution
- **第二次练习** (2nd attempt): Re-implementation after time interval
- **1more/2more/3more**: Reinforcement iterations for problem mastery
- Consider filenames or comments should indicate iteration level

### Testing Approach
- Most files have test calls at bottom: `print(function(test_input))`
- No formal test framework; inline execution for validation
- Enable/disable print statements via comments for debugging

### Code Style
- Type hints used but not enforced throughout codebase
- Chinese comments acceptable and common
- Document algorithm choice and time/space complexity when known
- Prioritize clarity over brevity in algorithm comments

## External References
- **LeetCode**: https://leetcode-cn.com/ (Chinese version, referenced in solutions)
- **Course Material**: "船长课程" (Captain's course) from kaikeba.com

## Workflow Tips for AI Agents

1. **Adding New Problems**: Create file in appropriate category directory following `NO_{id}_{name}_{difficulty}.py` format
2. **Multiple Solutions**: Include alternative approaches with clear method naming (`twoSum`, `twoSum2`, etc.) and comments explaining trade-offs
3. **Data Structure Reuse**: Check `linkedlist/myLinkedList.py` and similar utility modules before defining new base classes
4. **Algorithm Documentation**: Include problem understanding summary and recursion/DP logic explanation as docstring or leading comment block
5. **Cross-Module Patterns**: Reference solutions in same category for consistent style and approach patterns
