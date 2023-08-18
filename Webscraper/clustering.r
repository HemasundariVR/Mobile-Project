data <- read.csv(file.choose(),header = TRUE)

prod_star <- data$prod_star
data$prod_star <- NULL
prod_brand <- data$prod_brand
data$prod_brand <- NULL
prod_name <- data$prod_name
data$prod_name <- NULL
launch_date <- data$launch_date
data$launch_date <- NULL
product_availability <- data$product_availability
data$product_availability <- NULL
data$connectivity <- NULL

# Hierarchical Clustering
distance_matrix <- dist(data, method = "euclidean")
hierarchical_model <- hclust(distance_matrix, method = "ward.D2")

# Dendrogram Plot
plot(hierarchical_model, main = "Dendrogram of Mobile Phones", xlab = "Phones", sub = "", ylab = "Distance")
cluster_assignment<-cutree(hierarchical_model,k = 10 )


data$cluster <- cluster_assignment
prod_name -> data$prod_name
prod_brand -> data$prod_brand
prod_star -> data$prod_star
launch_date -> data$launch_date
product_availability ->  data$product_availability

write.csv(data, file = "D:/Project-1/Webscraper/cluster.csv", row.names = FALSE)

