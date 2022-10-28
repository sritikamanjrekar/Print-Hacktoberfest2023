class Solution {

public:

    int maxProduct(vector<int>& nums){

        

        long long int maxi=INT_MIN;

        long long int product=1;

    

        for(int i=0;i<nums.size();i++)

        {

            product*=nums[i];

            maxi=max(maxi,product);

            if(product==0)

                product=1;

        }

        product=1;

         for(int i=nums.size()-1;i>=0;i--)

        {

            product*=nums[i];

            maxi=max(maxi,product);

            if(product==0)

                product=1;

        }

        return maxi;

        

    }

};
        
