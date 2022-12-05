use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn main() 
{
   let mut arr_index: usize = 0;
   let mut sum_arr: [u32; 500] = [0;500];
   let mut rolling_sum: u32 = 0;
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("day1.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines 
        {
            if let Ok(data_line) = line 
            {
               if data_line.chars().count() < 3
               {
                  sum_arr[arr_index] = rolling_sum;
                  rolling_sum = 0;
                  arr_index += 1;
               }

               else
               {
                  // println!("{}", data_line);
                  // data_line.pop();
                  let temp_int: u32 = data_line.parse::<u32>().unwrap();
                  rolling_sum += temp_int
               }
               //  println!("{}", data_line);
            }
        }

         println!("{:?}", sum_arr);
         let mut max_sum: u32 = 0;
         let mut max_val: u32 = 0;
         let mut max_index: usize = 0;
         for _num_maxes in 0..3
         {
            for i in 0..500
            {
               let arr_val = sum_arr[i];
               if arr_val > max_val
               {
                  max_val = arr_val;
                  max_index = i;
               }
            }

            max_sum += max_val;
            sum_arr[max_index] = 0;
         }
         println!("MaxVal {}", max_val);
         println!("MaxSum {}", max_sum);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>where P: AsRef<Path>, 
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}