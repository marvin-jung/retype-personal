library(rtweet)
library(dplyr)
library(tidytext)
library(tidyverse)
library(ggplot2)
library(tidyr)

########################################################
### Explore for tweets for Music Streaming Services  ###
########################################################

data(stop_words)

# Build dataset of tweets of Apple and music
Spotify <- search_tweets(
  "#Spotify #music", n = 50000, include_rts = FALSE
)
tidy_Spotify <- Spotify %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

# counting frequencies for tokens
tidy_Spotify %>%
  count(word, sort=TRUE)

# Build dataset of tweets of Apple and music
Apple <- search_tweets(
  "#Apple #music", n = 50000, include_rts = FALSE
)
tidy_Apple <- Apple %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

# counting frequencies for tokens
tidy_Apple %>%
  count(word, sort=TRUE)

# Build dataset of tweets of YouTube and music
YouTube <- search_tweets(
  "#YouTube #music", n = 50000, include_rts = FALSE
)
tidy_YouTube <- YouTube %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

# counting frequencies for tokens
tidy_YouTube %>%
  count(word, sort=TRUE)

###################################################
#### Combine all the datasets and do frequencies ##
###################################################

frequency <- bind_rows(mutate(tidy_Spotify, service="Spotify"),
                       mutate(tidy_Apple, service= "Apple Music"),
                       mutate(tidy_YouTube, service="YouTube Music")
)%>%#closing bind_rows
  mutate(word=str_extract(word, "[a-z']+")) %>%
  count(service, word) %>%
  group_by(service) %>%
  mutate(proportion = n/sum(n))%>%
  select(-n) %>%
  spread(service, proportion) %>%
  gather(service, proportion, `Apple Music`, `YouTube Music`)

# Plot the correlograms:
library(scales)
ggplot(frequency, aes(x=proportion, y=`Spotify`, 
                      color = abs(`Spotify`- proportion)))+
  geom_abline(color="grey40", lty=2)+
  geom_jitter(alpha=.1, size=2.5, width=0.3, height=0.3)+
  geom_text(aes(label=word), check_overlap = TRUE, vjust=1.5) +
  scale_x_log10(labels = percent_format())+
  scale_y_log10(labels= percent_format())+
  scale_color_gradient(limits = c(0,0.001), low = "darkslategray4", high = "gray75")+
  facet_wrap(~service, ncol=2)+
  theme(legend.position = "none")+
  labs(y= "Spotify", x=NULL)

####################################
####   doing the cor.test()    #####
####################################

# Correlation index between Apple Music and Spotify
cor.test(data=frequency[frequency$service == "Apple Music",],
         ~proportion + `Spotify`)

# Correlation index between YouTube Music and Spotify
cor.test(data=frequency[frequency$service == "YouTube Music",],
         ~proportion + `Spotify`)

##########################################################################
## Plot common bigrams in Music Streaming Services, with some polishing ##                              ##
##########################################################################

library(textdata)
library(dplyr)
library(stringr)
library(tidyverse)
library(tidytext)
library(igraph)
library(ggraph)

### Spotify ###

Spotify_bigrams <- Spotify %>%
  unnest_tokens(bigram, text, token = "ngrams", n = 2) %>% 
  filter(!is.na(bigram)) %>% 
  count(bigram, sort = TRUE) %>% 
  separate(bigram, c("word1", "word2"), sep = " ") %>% 
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word)

bigram_graph <- Spotify_bigrams %>%
  filter(n>60) %>%
  graph_from_data_frame() 

a <- grid::arrow(type = "closed", length = unit(.15, "inches"))

ggraph(bigram_graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches')) +
  geom_node_point(color = "lightblue", size = 5) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()

### Apple Music ###

Apple_bigrams <- Apple %>%
  unnest_tokens(bigram, text, token = "ngrams", n = 2) %>% 
  filter(!is.na(bigram)) %>% 
  count(bigram, sort = TRUE) %>% 
  separate(bigram, c("word1", "word2"), sep = " ") %>% 
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word)

bigram_graph <- Apple_bigrams %>%
  filter(n>8) %>%
  graph_from_data_frame()

a <- grid::arrow(type = "closed", length = unit(.15, "inches"))

ggraph(bigram_graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches')) +
  geom_node_point(color = "lightblue", size = 5) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()

### YouTube Music ###

YouTube_bigrams <- YouTube %>%
  unnest_tokens(bigram, text, token = "ngrams", n = 2) %>% 
  filter(!is.na(bigram)) %>% 
  count(bigram, sort = TRUE) %>% 
  separate(bigram, c("word1", "word2"), sep = " ") %>% 
  filter(!word1 %in% stop_words$word) %>%
  filter(!word2 %in% stop_words$word)

bigram_graph <- YouTube_bigrams %>%
  filter(n>40) %>%
  graph_from_data_frame()

a <- grid::arrow(type = "closed", length = unit(.15, "inches"))

ggraph(bigram_graph, layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches')) +
  geom_node_point(color = "lightblue", size = 5) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()
