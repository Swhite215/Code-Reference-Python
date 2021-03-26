A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16]
C = [1 1; 2 2]

A*C % Matrix Multiplication
A .* B % Element Wise Multiplication
A .^ 2 % Element Wise Squaring

v = [1; 2; 3]
1 ./ v % Element Wise Reciprocal
1 ./ A % Element Wise Reciprocal

log(v) % Element Wise Logarithm
exp(v) % Base E Exponentiation
abs(v) % Element Wise Absolute Value of v
-v % Negative of v
v + ones(length(v), 1) % Increments v by 1
v + 1 % Scalar Addition

A' % Transpose of Matrix A
a = [1 15 2 0.5]
[val, ind] = max(a) % Returns Max Value and Index of Max of a
a < 3 % Element Wise Comparison
find(a < 3) % Find Elements Less than 3

A = magic(3) % Returns Magic Squares (Rows, Columns, and Diagonals Equal Sum)
sum(a) % Sum of Values
prod(a) % Prod of All values
floor(a) % Round Down All Values
ceil(a) % Round Up All Values

max(A, [], 1) % Column Wise Maximum
max(A, [], 2) % Per Row Maximums
max(max(A))

A = magic(9)
sum(A,1) % Sums All Columns
sum(A, 2) % Sums All Rows
A .*eye(9) % Element Wise Product Leaving Diagonals
sum(sum(A .*eye(9))) % Sums Values Diagonal

flipud(eye(9)) % Switches Diagonal
A = magic(3)
pinv(A) % Inverse of A