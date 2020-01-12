%%
% This is an example of how to add a horizontal colorbar to a plot in MATLAB&#174;.
% 
% Read about the <http://www.mathworks.com/help/matlab/ref/colorbar.html |colorbar|> function in the MATLAB documentation.
%
% For more examples, go to <http://www.mathworks.com/discovery/gallery.html MATLAB Plot Gallery>
%
% Copyright 2012-2014 The MathWorks, Inc.

% Load spine data
load spine X

% Create an image plot of the spine data
figure
imagesc(X)
colormap bone

% Add a horizontal colorbar to the bottom of the plot
colorbar('SouthOutside')
axis square
