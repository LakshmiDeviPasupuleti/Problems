class Solution {
    public boolean isPalindrome(String s) {
        if(s==null) return false;
        String clean=s.replaceAll("[^A-Za-z0-9]","").toLowerCase();
        int left=0;
        int right=clean.length()-1;
        while (left < right){
            if (clean.charAt(left++)!=clean.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}