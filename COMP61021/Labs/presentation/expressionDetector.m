load('Yale_64x64')
load('expressionLabels.mat')

training = struct('data',[],'labels',[]);
testing = struct('data',[],'labels',[]);
for i = 1:size(gnd)
    personId = gnd(i);
    
    if(personId == 1)
        % Add to test
        testing.data = [testing.data; fea(i,:)];
        testing.labels = [testing.labels; expressionLabels(i)];
    else
        % Add to training
        training.data = [training.data; fea(i,:)];
        training.labels = [training.labels; expressionLabels(i)];
    end
end



options = [];
options.Metric = 'Euclidean';
options.NeighborMode = 'Supervised';
options.gnd = training.labels;
options.WeightMode = 'HeatKernel';
options.t = 1;

W = constructW(training.data,options);

[eigvector, eigvalue, Y] = LPP(training.data, W, options);

trainingSize = size(training.labels);

% % display all happy laplacian faces
% for i = 1:size(training.labels)
%     if(training.labels(i) == 1)
%        figure;
%        displayFace(eigvector(:,trainingSize(1) - i));
%     end
% end

% find a happy test face
for i = 1:size(testing.labels)
   if(testing.labels(i) == 1)
       testFace = testing.data(i,:);
       break;
   end
end

% testLaplacianFace = testFace'*W*testFace;