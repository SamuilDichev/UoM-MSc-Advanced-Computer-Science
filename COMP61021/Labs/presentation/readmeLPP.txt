Q & A:

Q: How to use the code?

A: You need to put LPP.m, PCA.m in your working directory. If you want to use constrctW to 
   construct the affinity matrix, you should also put constructW.m in your working directory.
   
   'help LPP' for detail information.
   'help constructW' for details on how to construct the affinity matrix.    
        
        
Q: Why LPP code does not work in my application?

A: If the number of samples is much larger than the number of features, you might need to use the 
   Kernel LPP.
   
   The affinity graph construction plays a key role, you might need to constuct the affinity 
   matrix by your own (based on your knowledge of your application). Please refer the following
   papers. 

   
Reference:
	Xiaofei He, and Partha Niyogi, "Locality Preserving Projections"
	Advances in Neural Information Processing Systems 16 (NIPS 2003),
	Vancouver, Canada, 2003.

   Xiaofei He, Shuicheng Yan, Yuxiao Hu, Partha Niyogi, and Hong-Jiang Zhang,   
   "Face Recognition Using Laplacianfaces", IEEE PAMI, Vol. 27, No. 3, Mar.  2005.

   Deng Cai, Xiaofei He and Jiawei Han, "Document Clustering Using Locality Preserving Indexing"
   IEEE TKDE, 2005.   
   
   Deng Cai, Xiaofei He and Jiawei Han, "Using Graph Model for Face Analysis",
   Technical Report, UIUCDCS-R-2005-2636, UIUC, Sept. 2005
   
   