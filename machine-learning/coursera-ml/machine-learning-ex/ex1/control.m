v = zeros(10, 1)
for i=1:10,
    v(i) = 2^i;
end;
v

% For Loop
indices=1:10;
for i=indices,
    disp(i);
end;

% While Loop
i = 1;
while i <= 5,
    v(i) = 100;
    i = i+1;
end;
v

% Using Break
i = 1;
while true,
    v(i) = 999;
    i = i+1;
    if i == 6,
        break;
    end;
end;
v

% If, ElseIf, Else
v(1) = 2;
if v(1) == 1,
    disp("ONE");
elseif v(1) == 2,
    disp("TWO");
else
    disp("NEITHER");
end;

% Functions
squareThisNumber(5)
[squared, cubed] = squareAndCubeThisNumber(5)

% Cost Function
X = [1 1; 1 2; 1 3];
y = [1; 2; 3];

theta = [0;1];
j = costFunctionJ(X, y, theta)
theta = [0;0];
j = costFunctionJ(X, y, theta)