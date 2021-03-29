def godSaveTheQueen( ratingList: list ):
	sortedRatingList = []
	for rating in ratingList:
		if rating > 40:
			roundedFive = int(5 * round(float(rating) / 5)) # Calculate the closest multiple of 5
			if (roundedFive - rating) < 3:
				rating = roundedFive
		if rating == 40: 
			print("nul germain nul")
		sortedRatingList.append(rating)
	return sortedRatingList

print(godSaveTheQueen([43, 83, 90, 33, 79, 22, 34, 40]))
