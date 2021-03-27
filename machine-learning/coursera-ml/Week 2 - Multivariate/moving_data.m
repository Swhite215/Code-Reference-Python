load ex1data2.txt

who % Shows Variables in Memory

ex1data2 % Data
size(ex1data2) % Dimensions of Loaded Data

whos % Detailed View of Variables

v = ex1data2(1:10) % Row Vector
t = v' % Column Vector

save hello.mat t & Saves Data in Binary Format

clear ex1data2 % Clears Variables

whos % Detailed View of Variables

clear % Clears All Workspace Variables

whos % Detailed View of Variables

load hello.mat

whos % Detailed View of Variables

t

save hello.txt t -ascii % Saves as Human Readable

A = [1,2;3,4;5,6]
A(3,2) % Returns 6
A(2,:) % Returns Every Element in Second Row
A(:, 2) % Returns Every Element in Second Column
A([1 3], :) % Get Every Element from 1st and 3rd Rows
A(:,2) = [10; 11; 12] % Assign and Replace Second Column
A = [A, [100; 101; 102]] % Appends Column to Matrix A
A(:) % Put All Elements of A into Single Column Vector

A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16]
C = [A B] % Concatenating Matrices Side by Side
C = [A; B] % Concatenates Matrices Top and Bottom
