    What is the usability score of this dataset and is it “good” or “bad”?
    How is this usability score calculated?
    What are the two credibility issues with this dataset and why are they important?
    How many columns does this dataset have?
    What is the licence for this dataset and how would you summarise the usage rights in your own words?

1. 8.82. Good <br/>
2. Completeness (Subtitle, Tag, Description, Cover Image), Credibility (Source/Provenance, Public Notebook, Update Frequency), Compatibility (Licence, File Format, File Description, Column Description)<br/>
3. Source/Provenance, Update Frequency. If you can't trust the origin of the data, you can't trust the validity of the data. Lack of updates could mean data is out of date.<br/>
4. 35<br/>
5. Database - Open Data Commons. Worldwide, royalty-free, non-exclusive, perpetual, irrevocable copyright license. Includes commercial use.<br/><br/><br/>

**What does MD5 mean?**<br/>
   
The MD5 message-digest algorithm is a widely used hash function producing a 128-bit hash value. <br/>
MD5 can be used as a checksum to verify data integrity against unintentional corruption<br/>


**What are the dataTypes sc:Integer and sc:Boolean? Find an example of a Boolean field.**<br/>
Integer - whole number.<br/>
Boolean - operator<br/>

**Why does using compression aid sustainability and net-zero goals?**<br/>
Compressed data is smaller data. Less data transferrance means less energy usage.<br/>


**What is the possible issue in identifying the meaning of the column named 'YearsSinceLastPromotion', especially when interpreting the value of '0' in one of the fields?**<br/>
Does not specify if it is inclusive of Year 0? (unsure)

**Compare the contents of the column 'Over18' and 'OverTime', what data quality issue can you identify?**<br/>
Over18 is all Y, no N. Possible accuracy issue. They also use a different notation to mean the same thing (Y vs Yes). Consistency issue. <br/>

**What are some possible issues with the data quality of 'MonthlyIncome' and 'Monthly Rate'?**<br/>
Integers instead of decimals could mean data lost.<br/>

**How would you validate the 'EmployeeNumber' column and what needs paying special attention to?**<br/>
No idea what this question is intending. The IDs seem roughly sequential but the IDs go higher than colleage total. Likely just due to turnover. Need to ensure they are kept as integers to allow sorting.<br/>
