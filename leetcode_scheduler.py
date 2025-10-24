import json
import datetime
from collections import defaultdict
import random
import os

# NeetCode 150 problems organized by category
PROBLEMS = {
    "Arrays & Hashing": [
        {"id": 217, "name": "Contains Duplicate"},
        {"id": 242, "name": "Valid Anagram"},
        {"id": 1, "name": "Two Sum"},
        {"id": 49, "name": "Group Anagrams"},
        {"id": 347, "name": "Top K Frequent Elements"},
        {"id": 238, "name": "Product of Array Except Self"},
        {"id": 36, "name": "Valid Sudoku"},
        {"id": 271, "name": "Encode And Decode Strings"},
        {"id": 128, "name": "Longest Consecutive Sequence"},
    ],
    "Two Pointers": [
        {"id": 125, "name": "Valid Palindrome"},
        {"id": 167, "name": "Two Sum II Input Array Is Sorted"},
        {"id": 15, "name": "3Sum"},
        {"id": 11, "name": "Container With Most Water"},
        {"id": 42, "name": "Trapping Rain Water"},
    ],
    "Sliding Window": [
        {"id": 121, "name": "Best Time to Buy And Sell Stock"},
        {"id": 3, "name": "Longest Substring Without Repeating Characters"},
        {"id": 424, "name": "Longest Repeating Character Replacement"},
        {"id": 567, "name": "Permutation In String"},
        {"id": 76, "name": "Minimum Window Substring"},
        {"id": 239, "name": "Sliding Window Maximum"},
    ],
    "Stack": [
        {"id": 20, "name": "Valid Parentheses"},
        {"id": 155, "name": "Min Stack"},
        {"id": 150, "name": "Evaluate Reverse Polish Notation"},
        {"id": 22, "name": "Generate Parentheses"},
        {"id": 739, "name": "Daily Temperatures"},
        {"id": 853, "name": "Car Fleet"},
        {"id": 84, "name": "Largest Rectangle In Histogram"},
    ],
    "Binary Search": [
        {"id": 704, "name": "Binary Search"},
        {"id": 74, "name": "Search a 2D Matrix"},
        {"id": 875, "name": "Koko Eating Bananas"},
        {"id": 33, "name": "Search In Rotated Sorted Array"},
        {"id": 153, "name": "Find Minimum In Rotated Sorted Array"},
        {"id": 981, "name": "Time Based Key Value Store"},
        {"id": 4, "name": "Median of Two Sorted Arrays"},
    ],
    "Linked List": [
        {"id": 206, "name": "Reverse Linked List"},
        {"id": 21, "name": "Merge Two Sorted Lists"},
        {"id": 143, "name": "Reorder List"},
        {"id": 19, "name": "Remove Nth Node From End of List"},
        {"id": 138, "name": "Copy List With Random Pointer"},
        {"id": 2, "name": "Add Two Numbers"},
        {"id": 141, "name": "Linked List Cycle"},
        {"id": 287, "name": "Find The Duplicate Number"},
        {"id": 146, "name": "LRU Cache"},
        {"id": 23, "name": "Merge K Sorted Lists"},
        {"id": 25, "name": "Reverse Nodes In K Group"},
    ],
    "Trees": [
        {"id": 226, "name": "Invert Binary Tree"},
        {"id": 104, "name": "Maximum Depth of Binary Tree"},
        {"id": 543, "name": "Diameter of Binary Tree"},
        {"id": 110, "name": "Balanced Binary Tree"},
        {"id": 100, "name": "Same Tree"},
        {"id": 572, "name": "Subtree of Another Tree"},
        {"id": 235, "name": "Lowest Common Ancestor of a Binary Search Tree"},
        {"id": 102, "name": "Binary Tree Level Order Traversal"},
        {"id": 199, "name": "Binary Tree Right Side View"},
        {"id": 1448, "name": "Count Good Nodes In Binary Tree"},
        {"id": 98, "name": "Validate Binary Search Tree"},
        {"id": 230, "name": "Kth Smallest Element In a Bst"},
        {"id": 105, "name": "Construct Binary Tree From Preorder And Inorder Traversal"},
        {"id": 124, "name": "Binary Tree Maximum Path Sum"},
        {"id": 297, "name": "Serialize And Deserialize Binary Tree"},
    ],
    "Tries": [
        {"id": 208, "name": "Implement Trie Prefix Tree"},
        {"id": 211, "name": "Design Add And Search Words Data Structure"},
        {"id": 212, "name": "Word Search II"},
    ],
    "Heap / Priority Queue": [
        {"id": 703, "name": "Kth Largest Element In a Stream"},
        {"id": 1046, "name": "Last Stone Weight"},
        {"id": 973, "name": "K Closest Points to Origin"},
        {"id": 215, "name": "Kth Largest Element In An Array"},
        {"id": 621, "name": "Task Scheduler"},
        {"id": 355, "name": "Design Twitter"},
        {"id": 295, "name": "Find Median From Data Stream"},
    ],
    "Backtracking": [
        {"id": 78, "name": "Subsets"},
        {"id": 39, "name": "Combination Sum"},
        {"id": 46, "name": "Permutations"},
        {"id": 90, "name": "Subsets II"},
        {"id": 40, "name": "Combination Sum II"},
        {"id": 79, "name": "Word Search"},
        {"id": 131, "name": "Palindrome Partitioning"},
        {"id": 17, "name": "Letter Combinations of a Phone Number"},
        {"id": 51, "name": "N Queens"},
    ],
    "Graphs": [
        {"id": 200, "name": "Number of Islands"},
        {"id": 133, "name": "Clone Graph"},
        {"id": 695, "name": "Max Area of Island"},
        {"id": 417, "name": "Pacific Atlantic Water Flow"},
        {"id": 130, "name": "Surrounded Regions"},
        {"id": 994, "name": "Rotting Oranges"},
        {"id": 286, "name": "Walls And Gates"},
        {"id": 207, "name": "Course Schedule"},
        {"id": 210, "name": "Course Schedule II"},
        {"id": 684, "name": "Redundant Connection"},
        {"id": 323, "name": "Number of Connected Components In An Undirected Graph"},
        {"id": 261, "name": "Graph Valid Tree"},
        {"id": 127, "name": "Word Ladder"},
    ],
    "Advanced Graphs": [
        {"id": 332, "name": "Reconstruct Itinerary"},
        {"id": 1584, "name": "Min Cost to Connect All Points"},
        {"id": 743, "name": "Network Delay Time"},
        {"id": 778, "name": "Swim In Rising Water"},
        {"id": 269, "name": "Alien Dictionary"},
        {"id": 787, "name": "Cheapest Flights Within K Stops"},
    ],
    "1-D Dynamic Programming": [
        {"id": 70, "name": "Climbing Stairs"},
        {"id": 746, "name": "Min Cost Climbing Stairs"},
        {"id": 198, "name": "House Robber"},
        {"id": 213, "name": "House Robber II"},
        {"id": 5, "name": "Longest Palindromic Substring"},
        {"id": 647, "name": "Palindromic Substrings"},
        {"id": 91, "name": "Decode Ways"},
        {"id": 322, "name": "Coin Change"},
        {"id": 152, "name": "Maximum Product Subarray"},
        {"id": 139, "name": "Word Break"},
        {"id": 300, "name": "Longest Increasing Subsequence"},
        {"id": 416, "name": "Partition Equal Subset Sum"},
    ],
    "2-D Dynamic Programming": [
        {"id": 62, "name": "Unique Paths"},
        {"id": 1143, "name": "Longest Common Subsequence"},
        {"id": 309, "name": "Best Time to Buy And Sell Stock With Cooldown"},
        {"id": 518, "name": "Coin Change II"},
        {"id": 494, "name": "Target Sum"},
        {"id": 97, "name": "Interleaving String"},
        {"id": 329, "name": "Longest Increasing Path In a Matrix"},
        {"id": 115, "name": "Distinct Subsequences"},
        {"id": 72, "name": "Edit Distance"},
        {"id": 312, "name": "Burst Balloons"},
        {"id": 10, "name": "Regular Expression Matching"},
    ],
    "Greedy": [
        {"id": 53, "name": "Maximum Subarray"},
        {"id": 55, "name": "Jump Game"},
        {"id": 45, "name": "Jump Game II"},
        {"id": 134, "name": "Gas Station"},
        {"id": 846, "name": "Hand of Straights"},
        {"id": 1899, "name": "Merge Triplets to Form Target Triplet"},
        {"id": 763, "name": "Partition Labels"},
        {"id": 678, "name": "Valid Parenthesis String"},
    ],
    "Intervals": [
        {"id": 57, "name": "Insert Interval"},
        {"id": 56, "name": "Merge Intervals"},
        {"id": 435, "name": "Non Overlapping Intervals"},
        {"id": 252, "name": "Meeting Rooms"},
        {"id": 253, "name": "Meeting Rooms II"},
        {"id": 1851, "name": "Minimum Interval to Include Each Query"},
    ],
    "Math & Geometry": [
        {"id": 48, "name": "Rotate Image"},
        {"id": 54, "name": "Spiral Matrix"},
        {"id": 73, "name": "Set Matrix Zeroes"},
        {"id": 202, "name": "Happy Number"},
        {"id": 66, "name": "Plus One"},
        {"id": 50, "name": "Pow(x, n)"},
        {"id": 43, "name": "Multiply Strings"},
        {"id": 2013, "name": "Detect Squares"},
    ],
    "Bit Manipulation": [
        {"id": 136, "name": "Single Number"},
        {"id": 191, "name": "Number of 1 Bits"},
        {"id": 338, "name": "Counting Bits"},
        {"id": 190, "name": "Reverse Bits"},
        {"id": 268, "name": "Missing Number"},
        {"id": 371, "name": "Sum of Two Integers"},
        {"id": 7, "name": "Reverse Integer"},
    ]
}

# Define fixed category order
CATEGORY_ORDER = [
    "Arrays & Hashing",
    "Two Pointers",
    "Sliding Window",
    "Stack",
    "Binary Search",
    "Linked List",
    "Trees",
    "Tries",
    "Heap / Priority Queue",
    "Backtracking",
    "Graphs",
    "Advanced Graphs",
    "1-D Dynamic Programming",
    "2-D Dynamic Programming",
    "Greedy",
    "Intervals",
    "Math & Geometry",
    "Bit Manipulation"
]

DATA_FILE = "leetcode_progress.json"

def get_next_weekday(date):
    """Return the next weekday (Monday-Friday) after the given date."""
    next_day = date + datetime.timedelta(days=1)
    while next_day.weekday() >= 5:  # Saturday (5) or Sunday (6)
        next_day += datetime.timedelta(days=1)
    return next_day

def load_progress():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Initialize progress for all problems
    progress = {
        "last_run": None,
        "category_index": 0,
        "pending_problems": [],
        "cycle_count": 0,
        "cycle_start_date": None
    }
    for category, problems in PROBLEMS.items():
        for problem in problems:
            pid = str(problem["id"])
            progress[pid] = {
                "name": problem["name"],
                "category": category,
                "last_attempted": None,
                "next_review": datetime.datetime.now().date().isoformat(),
                "success_count": 0,
                "fail_count": 0,
                "interval_days": 7,
                "cycle_completed_count": 0  # Track completions per cycle
            }
    return progress

def save_progress(progress):
    with open(DATA_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def check_missed_days(progress, today):
    """Reschedule problems from missed days to today."""
    if progress.get("last_run") is None:
        return
    last_run = datetime.date.fromisoformat(progress["last_run"])
    if last_run >= today:
        return
    current = last_run + datetime.timedelta(days=1)
    while current <= today:
        if current.weekday() < 5:
            for pid, data in progress.items():
                if pid in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]:
                    continue
                next_review = datetime.date.fromisoformat(data["next_review"])
                if next_review <= current:
                    data["next_review"] = today.isoformat()
        current += datetime.timedelta(days=1)

def get_due_problems(progress, today):
    due = []
    for pid, data in progress.items():
        if pid in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]:
            continue
        next_review = datetime.date.fromisoformat(data["next_review"])
        last_attempted = data.get("last_attempted")
        if last_attempted and last_attempted == today.isoformat():
            continue
        if next_review <= today:
            due.append((pid, data["category"], data["name"]))
    return due

def pull_future_problems(progress, today, current_due, max_problems=4):
    """Pull future problems to today if fewer than max_problems are due."""
    future_problems = []
    for pid, data in progress.items():
        if pid in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]:
            continue
        if (pid, data["category"], data["name"]) not in current_due:
            next_review = datetime.date.fromisoformat(data["next_review"])
            if next_review > today:
                future_problems.append((pid, data["category"], data["name"], next_review))
    
    # Sort by earliest review date
    future_problems.sort(key=lambda x: x[3])
    
    # Pull problems to fill up to max_problems
    pulled = []
    for pid, category, name, _ in future_problems:
        if len(current_due) + len(pulled) < max_problems:
            progress[pid]["next_review"] = today.isoformat()
            pulled.append((pid, category, name))
            # Shift subsequent problems forward
            next_date = get_next_weekday(today)
            for subsequent_pid, data in progress.items():
                if subsequent_pid in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]:
                    continue
                next_review = datetime.date.fromisoformat(data["next_review"])
                if next_review == today:
                    data["next_review"] = next_date.isoformat()
        else:
            break
    return pulled

def select_category(due_problems, today, progress):
    # Group due problems by category
    categories = defaultdict(list)
    for pid, category, name in due_problems:
        categories[category].append((pid, name))
    
    total_problems = sum(len(problems) for problems in PROBLEMS.values())
    remaining_problems = sum(1 for pid, data in progress.items() 
                            if pid not in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"] 
                            and data["cycle_completed_count"] == progress.get("cycle_count", 0))
    
    # If 4 or fewer problems remain in the cycle, only select those
    max_problems = min(4, remaining_problems)
    
    if not categories and not progress.get("pending_problems"):
        return None, [], max_problems
    
    # Prioritize pending problems from the previous session
    pending = progress.get("pending_problems", [])
    selected_problems = []
    selected_category = None
    
    if pending:
        selected_category = progress[pending[0]]["category"]
        selected_problems = [(pid, progress[pid]["name"]) for pid in pending]
        progress["pending_problems"] = []
    
    if len(selected_problems) < max_problems:
        category_index = progress.get("category_index", 0)
        next_category = CATEGORY_ORDER[category_index]
        
        problems = categories.get(next_category, [])
        if not problems:
            for i in range(1, len(CATEGORY_ORDER)):
                next_category = CATEGORY_ORDER[(category_index + i) % len(CATEGORY_ORDER)]
                if next_category in categories:
                    problems = categories[next_category]
                    break
        
        problems.sort(key=lambda x: progress[x[0]].get("fail_count", 0), reverse=True)
        
        remaining_slots = max_problems - len(selected_problems)
        selected_problems.extend(problems[:remaining_slots])
        
        for pid, _ in problems[remaining_slots:]:
            progress[pid]["next_review"] = get_next_weekday(today).isoformat()
        
        if not selected_category and selected_problems:
            selected_category = progress[selected_problems[0][0]]["category"]
        
        progress["category_index"] = (category_index + 1) % len(CATEGORY_ORDER)
    
    return selected_category, selected_problems, max_problems

def schedule_problem(progress, pid, success, today):
    data = progress[pid]
    data["last_attempted"] = today.isoformat()
    if success:
        data["success_count"] += 1
        data["cycle_completed_count"] += 1
        data["interval_days"] = 7 if data["success_count"] == 1 else data["interval_days"] * 2
        next_review = today + datetime.timedelta(days=data["interval_days"])
        data["next_review"] = get_next_weekday(next_review - datetime.timedelta(days=1)).isoformat()
    else:
        data["fail_count"] += 1
        next_review = today + datetime.timedelta(days=2)
        data["next_review"] = get_next_weekday(next_review - datetime.timedelta(days=1)).isoformat()

def check_cycle_completion(progress, today):
    total_problems = sum(len(problems) for problems in PROBLEMS.values())
    completed = sum(1 for pid, data in progress.items() 
                    if pid not in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"] 
                    and data["cycle_completed_count"] > progress.get("cycle_count", 0))
    
    if completed == total_problems:
        cycle_start = datetime.date.fromisoformat(progress["cycle_start_date"]) if progress.get("cycle_start_date") else today
        time_taken = (today - cycle_start).days
        print(f"\nCycle {progress['cycle_count'] + 1} completed!")
        print(f"Time taken: {time_taken} days")
        
        # Find top 5 worst-performing questions
        problems = [(pid, data["name"], data["fail_count"]) 
                    for pid, data in progress.items() 
                    if pid not in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]]
        problems.sort(key=lambda x: x[2], reverse=True)
        print("\nTop 5 worst-performing questions:")
        for i, (pid, name, fail_count) in enumerate(problems[:5], 1):
            print(f"{i}. LeetCode #{pid}: {name} (Failed {fail_count} times)")
        
        # Start new cycle
        progress["cycle_count"] = progress.get("cycle_count", 0) + 1
        progress["cycle_start_date"] = get_next_weekday(today).isoformat()
        for pid, data in progress.items():
            if pid in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"]:
                continue
            data["next_review"] = progress["cycle_start_date"]
            data["interval_days"] = 7

def main():
    today = datetime.datetime.now().date()
    if today.weekday() >= 5:
        print("Program only runs on weekdays. Please run on Monday-Friday.")
        return
    
    progress = load_progress()
    
    if progress.get("last_run"):
        last_run = datetime.date.fromisoformat(progress["last_run"])
        if (today - last_run).days >= 14:
            while True:
                response = input("It has been over 2 weeks since your last session. Would you like to continue with previous progress (c) or start new progress (n)? ").lower()
                if response in ['c', 'n']:
                    break
                print("Please enter 'c' or 'n'.")
            if response == 'n':
                progress = {
                    "last_run": None,
                    "category_index": 0,
                    "pending_problems": [],
                    "cycle_count": 0,
                    "cycle_start_date": today.isoformat()
                }
                for category, problems in PROBLEMS.items():
                    for problem in problems:
                        pid = str(problem["id"])
                        progress[pid] = {
                            "name": problem["name"],
                            "category": category,
                            "last_attempted": None,
                            "next_review": today.isoformat(),
                            "success_count": 0,
                            "fail_count": 0,
                            "interval_days": 7,
                            "cycle_completed_count": 0
                        }
    
    check_missed_days(progress, today)
    progress["last_run"] = today.isoformat()
    if not progress.get("cycle_start_date"):
        progress["cycle_start_date"] = today.isoformat()
    
    due_problems = get_due_problems(progress, today)
    remaining_problems = sum(1 for pid, data in progress.items() 
                            if pid not in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"] 
                            and data["cycle_completed_count"] == progress.get("cycle_count", 0))
    
    if remaining_problems <= 4:
        due_problems = [(pid, data["category"], data["name"]) 
                        for pid, data in progress.items() 
                        if pid not in ["last_run", "category_index", "pending_problems", "cycle_count", "cycle_start_date"] 
                        and data["cycle_completed_count"] == progress.get("cycle_count", 0)]
    else:
        if len(due_problems) + len(progress.get("pending_problems", [])) < 4:
            due_problems.extend(pull_future_problems(progress, today, due_problems))
    
    if not due_problems and not progress.get("pending_problems"):
        print("No problems due today.")
        return
    
    category, selected_problems, max_problems = select_category(due_problems, today, progress)
    if not selected_problems:
        print("No problems due today.")
        return
    
    print(f"\nToday's category: {category}")
    print(f"Problems to solve today (up to {max_problems}):")
    for i, (pid, name) in enumerate(selected_problems, 1):
        print(f"{i}. LeetCode #{pid}: {name}")
    
    print("\nEnter solve outcomes (y for success, n for failure, q to quit):")
    pending = []
    for pid, name in selected_problems:
        while True:
            response = input(f"Did you solve LeetCode #{pid}: {name}? (y/n/q): ").lower()
            if response in ['y', 'n', 'q']:
                break
            print("Please enter 'y', 'n', or 'q'.")
        
        if response == 'q':
            pending.append(pid)
            pending.extend(p[0] for p in selected_problems[selected_problems.index((pid, name))+1:])
            break
        success = response == 'y'
        schedule_problem(progress, pid, success, today)
    
    if pending:
        progress["pending_problems"] = pending
        for pid in pending:
            progress[pid]["next_review"] = get_next_weekday(today).isoformat()
    
    check_cycle_completion(progress, today)
    save_progress(progress)

if __name__ == "__main__":
    main()