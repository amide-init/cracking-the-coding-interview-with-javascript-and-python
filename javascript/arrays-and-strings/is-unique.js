// implement an algorithms to determine if a string has all unique characters.
// what if you cannot use additional data structure ?

function isUnique(str) {
   const arr  = new Array(128).fill(0);
   for(let i=0;i<str.length;i++){
       if( arr[str.charCodeAt(i)] > 0)
         return "All character NOT  is unique in " + str ;
         arr[str.charCodeAt(i)] +=1;
   }
   return "All character is unique in " + str ;

}
console.log(isUnique("aminuddin"));
