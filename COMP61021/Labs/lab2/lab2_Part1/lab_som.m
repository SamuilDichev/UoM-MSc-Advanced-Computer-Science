function som = lab_som (trainingData, neuronCount, trainingSteps, startLearningRate, startRadius)
% som = lab_som (trainingData, neuronCount, trainingSteps, startLearningRate, startRadius)
% -- Purpose: Trains a 1D SOM i.e. A SOM where the neurons are arranged
%             in a single line. 
%             
% -- <trainingData> data to train the SOM with
% -- <som> returns the neuron weights after training
% -- <neuronCount> number of neurons 
% -- <trainingSteps> number of training steps 
% -- <startLearningRate> initial learning rate
% -- <startRadius> initial radius used to specify the initial neighbourhood size

dataDim = size(trainingData, 2);
som = rand(neuronCount, dataDim);
radius = startRadius;
learningRate = startLearningRate;

% Time constant
lambda = trainingSteps / log(startRadius);

% Draw all data
%%% scatter(trainingData(:, 1), trainingData(:, 2), 'b.');
%%% hold on;

for i = 1: trainingSteps
    %%% scatter(trainingData(:, 1), trainingData(:, 2), 'b.');
    %%% hold on;
    
    x = trainingData(randperm(size(trainingData, 1), 1), :);
    
    % Draw the point at this iteration
    %%% scatter(x(:, 1), x(:, 2), 'ro');

    % Get BMU
    bmuIdx = 1;
    for j = 2: size(som, 1)
        currDist = norm(som(j, :) - x);
        prevDist = norm(som(bmuIdx, :) - x);

        if currDist < prevDist
            bmuIdx = j;
        end
    end
    
    % Draw the neurons
    %%% scatter(som(:, 1), som(:, 2), 'g*');
    % Draw BMU
    %%% scatter(som(bmuIdx, 1), som(bmuIdx, 2), 'r*');
    
    for j = 1: size(som, 1)
        % get distance of neuron to the BMU
        % distToBMU = norm(som(bmuIdx, :) - som(j, :));
        if bmuIdx > j
            distToBMU = bmuIdx - j;
        else
            distToBMU = j - bmuIdx;
        end
        
        % if neuron is within the neighbourhood, adjust weight
        if distToBMU < radius
            
            % Draw neighbour
            oldPos = som(j, :);
            %%% scatter(som(j, 1), som(j, 2), 'y*');

            % calculate influence of learning rate on the neighbour, based
            % on how close the neighbour is to the BMU
            theta = exp(-(distToBMU^2) / (2*radius^2));
            
            % Adjust weight if in neighbourhood
            som(j, :) = som(j, :) + (learningRate * theta * (x - som(j, :)));
            
            % Draw new position and arrow between old and new
            %%% scatter(som(j, 1), som(j, 2), 'y*');
            %%% dp = som(j, :) - oldPos;
            %%% quiver(oldPos(:, 1), oldPos(:, 2), dp(:, 1), dp(:, 2), 0);
        end
    end
    
    % Decrease learning rate
    learningRate = startLearningRate * exp(-(i/trainingSteps));
    
    % Decrement neighbourhood size
    radius = startRadius * exp(-(i/trainingSteps));
    
    % hold off;
end
