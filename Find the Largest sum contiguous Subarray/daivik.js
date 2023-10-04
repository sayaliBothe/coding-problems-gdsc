//using kadane's algorithm
function largestSumSubArray(arr){
    let sum=0;
    let max=Number.MIN_SAFE_INTEGER;
    let n=arr.length;
    for (let i=0; i<n ; i++) {
        sum+=arr[i];
         if(sum<0){
            sum=0;
        }
        if(sum>max){
            max=sum;
        }
    }
    return max;
}

largestSumSubArray([1,2,-6,10,-100,50])//returns 50
