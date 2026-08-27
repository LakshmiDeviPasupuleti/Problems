class Solution {
    private boolean kokocaneat(int[] piles,int k,int h){
        int hour=0;
        for(int p:piles){
            hour +=(p+k-1)/k;
            if(hour>h)
            return false;
        }
        return hour <=h;

    }
    public int minEatingSpeed(int[] piles, int h) {
        int low_k=1;
        int high_k=-1;
        for (int n:piles)
        {
            high_k=Math.max(high_k,n);
        }
        int final_k=0;
        while (low_k < high_k){
            int mid=(low_k+high_k)/2;
            if(kokocaneat(piles,mid,h)){
                high_k=mid;
            }
            else{
                low_k=mid+1;
            }
        }
        return low_k;
        
    }
}