#!/bin/bash
Archive_DIR="archive"

#checking if the archive directory exits, create it if it doesn't exits
if [ ! -d $Archive_DIR ]; then
	mkdir "$Archive_DIR"
	echo "Create archive directory: $Archive_DIR"
else
	echo "Archive directory already exits: $Archive_DIR"
fi

#Generating the timestamp
Timestamp=$(date +"%Y%m%d-%H%M%S")
echo "Timestamp = $Timestamp"

#Archiving
Existing_file="grades.csv"
if [ -f "$Existing_file" ]; then
	New_file="grades_$Timestamp.csv"
	echo "the file $Existing_file has beign renamed to $New_file"

        mv $Existing_file $Archive_DIR/$New_file 
        echo "Archives $Existing_file as $Archive_DIR/$New_file"

	#wokspace Reset: creating an empty grades.csv file
        touch $Existing_file
	echo "Created a new empty file :$Existing_file"

	#Logging:appending details to organizer.log
	Log_file="organizer.log"
	echo "$Timestamp | original: $Existing_file | archived as: $Aechive_DIR/$NEW_file" >> "$Log_file"
        echo "Logged this operation to $Log_file"
else
    echo "Error: $SOURCE_FILE not found. Nothing to archive."
fi
