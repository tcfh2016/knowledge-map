// ZeroMatrixRowAndColumn.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <set>

#define ROW_NUM    3
#define COLUMN_NUM 4

void clearRowAndColumn(int matrix[ROW_NUM][COLUMN_NUM], int row, int col)
{
	for (int i = 0; i < COLUMN_NUM; ++i)
	{
		matrix[row][i] = 0;
	}

	for (int i = 0; i < ROW_NUM; ++i)
	{
		matrix[i][col] = 0;
	}
}

void zeroMatrixRowAndColumn(int matrix[ROW_NUM][COLUMN_NUM], int rows = ROW_NUM, int cols = COLUMN_NUM)
{
	std::set<int> zeroedRow;
	std::set<int> zeroedCol;

	for (int i = 0; i < rows; ++i)
	{
		for (int j = 0; j < cols; ++j)
		{
			if ((matrix[i][j] == 0) && (zeroedRow.find(i) == zeroedRow.end()) && (zeroedCol.find(j) == zeroedCol.end()))
			{
				zeroedRow.insert(i);
				zeroedCol.insert(j);

				clearRowAndColumn(matrix, i, j);
			}
		}
	}
}

void printMatrix(int matrix[][COLUMN_NUM], int row = ROW_NUM, int col = COLUMN_NUM)
{
	for (int i = 0; i < row; ++i)
	{
		for (int j = 0; j < col; ++j)
		{
			std::cout << matrix[i][j] << " ";			
		}
		std::cout << std::endl;
	}
}

int main()
{
	int test_matrix[ROW_NUM][COLUMN_NUM] = {\
		{1, 2, 3, 0}, \
		{1, 2, 1, 1}, \
		{1, 0, 3, 1} \
	};

	printMatrix(test_matrix, ROW_NUM, COLUMN_NUM);
	std::cout << "zero detecting..." << std::endl;
	zeroMatrixRowAndColumn(test_matrix, ROW_NUM, COLUMN_NUM);
	printMatrix(test_matrix, ROW_NUM, COLUMN_NUM);
	
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
