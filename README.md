Data dictionary

This is the data dictionary for our crime dataset. It can also be found here: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data

### 1. **ID**
- **Description**: Unique identifier for the record.
- **API Field Name**: `id`
- **Data Type**: Number

---

### 2. **Case Number**
- **Description**: The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
- **API Field Name**: `case_number`
- **Data Type**: Text

---

### 3. **Date**
- **Description**: Date when the incident occurred. This is sometimes a best estimate.
- **API Field Name**: `date`
- **Data Type**: Floating Timestamp

---

### 4. **Block**
- **Description**: The partially redacted address where the incident occurred, placing it on the same block as the actual address.
- **API Field Name**: `block`
- **Data Type**: Text

---

### 5. **IUCR**
- **Description**: The Illinois Uniform Crime Reporting code. This is directly linked to the Primary Type and Description.  
  [See the list of IUCR codes](https://data.cityofchicago.org/d/c7ck-438e).
- **API Field Name**: `iucr`
- **Data Type**: Text

---

### 6. **Primary Type**
- **Description**: The primary description of the IUCR code.
- **API Field Name**: `primary_type`
- **Data Type**: Text

---

### 7. **Description**
- **Description**: The secondary description of the IUCR code, a subcategory of the primary description.
- **API Field Name**: `description`
- **Data Type**: Text

---

### 8. **Location Description**
- **Description**: Description of the location where the incident occurred.
- **API Field Name**: `location_description`
- **Data Type**: Text

---

### 9. **Arrest**
- **Description**: Indicates whether an arrest was made.
- **API Field Name**: `arrest`
- **Data Type**: Checkbox

---

### 10. **Domestic**
- **Description**: Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
- **API Field Name**: `domestic`
- **Data Type**: Checkbox

---

### 11. **Beat**
- **Description**: Indicates the beat where the incident occurred. A beat is the smallest police geographic area.  
  [See the beats map](https://data.cityofchicago.org/d/aerh-rz74).
- **API Field Name**: `beat`
- **Data Type**: Text

---

### 12. **District**
- **Description**: Indicates the police district where the incident occurred.  
  [See the districts map](https://data.cityofchicago.org/d/fthy-xz3r).
- **API Field Name**: `district`
- **Data Type**: Text

---

### 13. **Ward**
- **Description**: The ward (City Council district) where the incident occurred.  
  [See the wards map](https://data.cityofchicago.org/d/sp34-6z76).
- **API Field Name**: `ward`
- **Data Type**: Number

---

### 14. **Community Area**
- **Description**: Indicates the community area where the incident occurred. Chicago has 77 community areas.  
  [See the community areas map](https://data.cityofchicago.org/d/cauq-8yn6).
- **API Field Name**: `community_area`
- **Data Type**: Text

---

### 15. **FBI Code**
- **Description**: Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS).  
  [See the FBI classifications](https://gis.chicagopolice.org/pages/crime_details).
- **API Field Name**: `fbi_code`
- **Data Type**: Text

---

### 16. **X Coordinate**
- **Description**: The x-coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection.  
  This location is shifted from the actual location for partial redaction but falls on the same block.
- **API Field Name**: `x_coordinate`
- **Data Type**: Number

---

### 17. **Y Coordinate**
- **Description**: The y-coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection.  
  This location is shifted from the actual location for partial redaction but falls on the same block.
- **API Field Name**: `y_coordinate`
- **Data Type**: Number

---

### 18. **Year**
- **Description**: The year the incident occurred.
- **API Field Name**: `year`
- **Data Type**: Number

---

### 19. **Updated On**
- **Description**: Date and time the record was last updated.
- **API Field Name**: `updated_on`
- **Data Type**: Floating Timestamp

---

### 20. **Latitude**
- **Description**: The latitude of the location where the incident occurred.  
  This location is shifted from the actual location for partial redaction but falls on the same block.
- **API Field Name**: `latitude`
- **Data Type**: Number

---

### 21. **Longitude**
- **Description**: The longitude of the location where the incident occurred.  
  This location is shifted from the actual location for partial redaction but falls on the same block.
- **API Field Name**: `longitude`
- **Data Type**: Number

---

### 22. **Location**
- **Description**: The location where the incident occurred in a format that allows for the creation of maps and other geographic operations on this data portal.  
  This location is shifted from the actual location for partial redaction but falls on the same block.
- **API Field Name**: `location`
- **Data Type**: Location

