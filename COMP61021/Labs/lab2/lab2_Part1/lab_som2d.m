function [som,grid] = lab_som2d (trainingData, neuronCountW, neuronCountH, trainingSteps, startLearningRate, startRadius)
% som = lab_som2d (trainingData, neuronCountW, neuronCountH, trainingSteps, startLearningRate, startRadius)
% -- Purpose: Trains a 2D SOM, which consists of a grid of
%             (neuronCountH * neuronCountW) neurons.
%             
% -- <trainingData> data to train the SOM with
% -- <som> returns the neuron weights after training
% -- <grid> returns the location of the neurons in the grid
% -- <neuronCountW> number of neurons along width
% -- <neuronCountH> number of neurons along height
% -- <trainingSteps> number of training steps 
% -- <startLearningRate> initial learning rate
% -- <startRadius> initial radius used to specify the initial neighbourhood size
%

dataDim = size(trainingData, 2);
neurons = neuronCountW * neuronCountH;
som = rand(neurons, dataDim);
radius = startRadius;
learningRate = startLearningRate;

grid = []
row = 1;
for h = 1: neuronCountH
    for w = 1: neuronCountW
        grid(row, 1) = h;
        grid(row, 2) = w;
        row = row + 1;
    end
end

% Time constant
lambda = trainingSteps / log(startRadius);

for i = 1: trainingSteps
    x = trainingData(randperm(size(trainingData, 1), 1), :);

    % Get BMU
    bmuIdx = 1;
    for j = 2: size(som, 1)
        currDist = norm(som(j, :) - x);
        prevDist = norm(som(bmuIdx, :) - x);

        if currDist < prevDist
            bmuIdx = j;
        end
    end
    
    for j = 1: size(som, 1)
        % get distance of neuron to the BMU
        % distToBMU = norm(som(bmuIdx, :) - som(j, :));
        distToBMU = sum(abs(grid(bmuIdx, :) - grid(j, :)));
        
        % if neuron is within the neighbourhood, adjust weight
        if distToBMU < radius
            % calculate influence of learning rate on the neighbour, based
            % on how close the neighbour is to the BMU
            theta = exp(-(distToBMU^2) / (2*radius^2));
            
            % Adjust weight if in neighbourhood
            som(j, :) = som(j, :) + (learningRate * theta * (x - som(j, :)));
        end
    end
    
    % Decrease learning rate
    learningRate = startLearningRate * exp(-(i/trainingSteps));
    
    % Decrement neighbourhood size
    radius = startRadius * exp(-(i/trainingSteps));
end

% TODO:
% The student will need to copy their code from lab_som() and
% update it so that it uses a 2D grid of neurons, rather than a 
% 1D line of neurons.
% 
% Your function will still return the a weight matrix 'som' with
% the same format as described in lab_som().
%
% However, it will additionally return a vector 'grid' that will
% state where each neuron is located in the 2D SOM grid. 
% 
% grid(n, :) contains the grid location of neuron 'n'
%
% For example, if grid = [[1,1];[1,2];[2,1];[2,2]] then:
% 
%   - som(1,:) are the weights for the neuron at position x=1,y=1 in the grid
%   - som(2,:) are the weights for the neuron at position x=2,y=1 in the grid
%   - som(3,:) are the weights for the neuron at position x=1,y=2 in the grid 
%   - som(4,:) are the weights for the neuron at position x=2,y=2 in the grid
%
% It is important to return the grid in the correct format so that
% lab_vis2d() can render the SOM correctly

