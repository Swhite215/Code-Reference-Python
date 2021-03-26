t = [0:0.01:0.98];
t
y1 = sin(2*pi*4*t)
plot(t, y1);

hold on; % Plots on Plots

y2 = cos(2*pi*4*t)
plot(t, y2, 'r');
xlabel('time') % X Axis Label
ylabel('value') % Y Axis Label
legend('sin', 'cos') % Legend
title('my plot') % Title
print -dpng 'myPlot.png' % Save Plot

clf; % Clears a Figure
A = magic(5)
imagesc(A)