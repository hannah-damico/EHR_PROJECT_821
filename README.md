# EHR_PROJECT_821
## End User Information
### Installation Instructions
   Begin by running the folllowing command line in your terminal:
         `install pytest`
   * Note that `pytest` should be installed in the working dirctory where testing will be run. The *testing_ehr_analysis* function will import `pytest`, so this step is important.
   
### Setup and Input File Instructions
   Download the three following necessary testing text files to working directory:
   1. *simple_test_data.txt*
      * Contains 4 columns, and 3 rows of generic, tab delimited testing data
   2. *patient_core_test_data.txt*
         * Contains 7 columns and 3 rows of tab delimited, fabricated EHR patient data
   3. *labs_core_test_data.txt*
      * Contains 6 columns and 6 rows of tab delimited, fabricated EHR patient data
   
   
### API description
   * **Authorization**: This documentation does not require authorization and may be implemented directly by following the above and below instructions.
   * **Resources**: All necessary resources for this documentation are include in this repository. No outside permissions or downloads are required.
   * **Error Messages**: Possible `ValueError` messages may be obtained from the function *sick_patients()* if users input labels other than those defined for use inthe function: "<" or ">". See example below:

      ```python
      print(sick_patients("CBC: PLATELET COUNT", "=", 4.0, labs_core_testing_data))
      ValueError(Unexpected label "=")
      ```
   * **Terms of use**: There are no legal constraints against the usage of this documentation as EHR (Electronic Health Record) records included for testing are fabricated purely for the use of testing.



## Contributor Information
### Testing Instructions
   Users should begin by opening python file *testing_ehr_analysis.py* and replacing pathways in each function corresponding to the correct text files per testing function as described below:
   1. *testing_parse_data( )*:
      * Variable *simple_test_data* should be replaced with user pathway corresponding to the textfile *simple_test_data.txt*

      ```python
      def testing_parse_data():
      """Check parse_data2 function coverage."""
      simple_test_data = "User/Pathway/Here"
      ```

   2. *testing_num_older_than( )*:
      * Variable *patient_core_test_data* should be replaced with user pathway corresponding to the textfile *patient_core_test_data.txt*
      ```python
      def testing_num_older_than():
      """Check num_older_than function coverage."""

      patient_core_test_data = parse_data("User/Pathway/Here")
      ```
   3. *testing_sick_patients( )*:
      * Variable *labs_core_test_data* should be replaced with user pathway corresponding to the textfile *labs_core_test_data.txt*

      ```python
      def testing_sick_patients():
      """Check sick_patients function coverage."""

      labs_core_test_data = parse_data("User/Pathway/Here")
      ```
   4. *testing_first_admission_age()*
      * Variable *patient_core_test_data* should be replaced with user pathway corresponding to the textfile *patient_core_test_data.txt*

      * Variable *labs_core_test_data* should be replaced with user pathway corresponding to the textfile *labs_core_test_data.txt*

      ```python
      def testing_first_admission_age():
      """Check first_admission_age function coverage."""

      patient_core_test_data = parse_data("User/Pathway/Here")
      labs_core_test_data = parse_data("User/Pathway/Here")
      ```

Once the above steps have been followed, users should open python file *ehr_analysis.py*. In the terminal, run the following command line:
   `pytest --cov . testing_ehr_analysis.py`

Testing Coverage will appear in terminal for users. To indicate lines missed in test, run `coverage report -m` in terminal after the above terminal command.

For more information information regarding `pytest` tesing options, visit:

https://pytest.org/en/latest/getting-started.html#assert-that-a-certain-exception-is-raised
