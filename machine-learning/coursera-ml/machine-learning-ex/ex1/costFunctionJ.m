function J = costFunctionJ(X, y, theta)

% X is the "design matrix" containing our training examples
% y is the class labels

m = size(X,1); % Number of training example
predictions = X*theta; % Predictions of hypothesis on all M examples
sqrErrors = (predictions - y).^2; % Squared Errors

J = 1/(2*m) * sum(sqrErrors);