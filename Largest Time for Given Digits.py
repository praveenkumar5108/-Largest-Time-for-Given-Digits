class Solution {
    public String largestTimeFromDigits(int[] A) {
        String res = "";
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                for(int k = 0; k < 4; k++){
                    if(i == j || j == k || k == i)
                        continue;
                    String HH = A[i] + "" + A[j];
                    String MM = A[k] + "" + A[6-i-j-k];
                    String Time = HH + ":" + MM;
                    if(HH.compareTo("24") < 0 && MM.compareTo("60")<0 && res.compareTo(Time)<0)
                        res = Time;
            }
            }
        }
        return res;
     
    }
}
