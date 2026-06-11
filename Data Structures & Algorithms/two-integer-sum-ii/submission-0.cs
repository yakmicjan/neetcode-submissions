public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int[] result = new int[2];
        int sum;
        int pointerX = 0;
        int pointerY = numbers.Length-1;

        while(pointerX < pointerY){
            sum = numbers[pointerX] + numbers[pointerY];
            if(sum > target)
                pointerY --;
            else if(sum < target)
                pointerX ++;
            else{
                result = [pointerX+1, pointerY+1];
                return result;
            }
        }
        return [0,0];

        // for(int i = 0; i < numbers.Length; i++){
        //     for(int y = numbers.Length-1; y > i; y--){
        //         sum = numbers[i] + numbers[y];
        //         if(sum > target)
        //             continue;
        //         else if(sum < target)
        //             break;
        //         else if(sum == target){
        //             result = [i+1, y+1];
        //             return result;
        //         }

        //     }
        // }
    }
}
