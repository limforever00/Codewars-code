// You live in the city of Cartesia where all roads are laid out in a perfect grid. 
// You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
// The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

// Note: you will always receive a valid array containing a random assortment of direction letters
//  ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
// n s e w 중 임의로 10개가 들어있는 배열 
// return true or false

function isValidWalk(arr) {
    if(arr.length != 10){
      return false;
    }
    
    // east&west south&north 각각 하나씩 변수사용해서 +- 해주면 변수 개수 줄일수있음
    // let cntE = 0
    // let cntW = 0
    // let cntS = 0
    // let cntN = 0

    let cntEW = 0
    let cntSN = 0
  
    for(var i=0; i<arr.length; i++){
        if(arr[i] == 'e'){
            // cntE++
            cntEW++
        }else if(arr[i] == 'w'){
            // cntW++
            cntEW--
        }else if(arr[i] == 's'){
            // cntS++
            cntSN++
        }else{
            // cntN++
            cntSN--
        }
    }
 
    // 위처럼 변수를 바꾸면 
    // if( cntE != cntW || cntS != cntN) {
    if( cntEW != 0 || cntSN != 0) {            
        return false;
    }
    
    return true;
}

