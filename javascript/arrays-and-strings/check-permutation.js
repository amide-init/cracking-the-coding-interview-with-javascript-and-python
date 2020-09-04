// Given two string, 
// write a method to decide if one is permutation of the other

// method 1 [by sorting the string]
// Time complexity O(nlogn)
function checkPermutation(str1, str2) {
   if(str1.length != str2.length)
      return false
   return str1.split('').sort().toString() == str2.split('').sort().toString()
}


console.log(checkPermutation("apple", "plee"))