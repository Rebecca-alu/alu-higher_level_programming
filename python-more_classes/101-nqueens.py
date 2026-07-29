#!/usr/bin/python3
"""Solves the N queens puzzle"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]"""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively try to place queens row by row"""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Entry point for the N queens program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == "__main__":
    main()
