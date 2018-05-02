install.packages("twitteR")
install.packages("wordcloud")
install.packages("plyr")
install.packages("dplyr")
install.packages("stringr")
install.packages("ggplot2")
install.packages("tm")
install.packages("RCurl")
install.packages("ROAuth")

# Clear the previously used libraries
#
 rm(list=ls())
#
# Load the required R libraries
#
 library(twitteR)
 library(ROAuth)
 library(RCurl)

#download.file(url="http://curl.haxx.se/ca/cacert.pem",destfile="cacert.pem")

#
# Set constant requestURL
#
  requestURL <- "https://api.twitter.com/oauth/request_token"
#
# Set constant accessURL
#
  accessURL <- "https://api.twitter.com/oauth/access_token"
#
# Set constant authURL
#
 authURL <- "https://api.twitter.com/oauth/authorize"


consumerKey <- ""
consumerSecret <- ""
accesstoken<-""
accesssecret<-""

twitCred <-setup_twitter_oauth(consumerKey , consumerSecret , accesstoken, accesssecret)

#Checking
#tweets <- searchTwitter("Obamacare OR ACA OR 'Affordable Care Act' OR #ACA", n=100, lang="en", since="2014-08-20")
 	
    library(plyr)
    library(dplyr)
    library(stringr)
    library(ggplot2)
    library(reshape2)
    library(twitteR)
    library(wordcloud)

    #Sentiment Package is not available on CRAN. You need to install it from archive.

 #   install.packages("devtools")
    require(devtools)
  #  install_url("http://cran.r-project.org/src/contrib/Archive/sentiment/sentiment_0.2.tar.gz")
    require(sentiment)
    ls("package:sentiment")

    # You have to make iteration to fetch all tweets. All the iterations are not mentioned in the code
    MI = searchTwitter("#CSK OR #CSKVSDD",since="2015-04-08",until="2015-04-09", n=3000,lang="en")
    KKR = searchTwitter("#DD OR #DDVSCSK", since="2015-04-08",until="2015-04-09",n=3000, lan="en")

    # get the text
    KKR_txt = sapply( unlist(KKR) , function(x) '$'( x , "text"))
    MI_txt = sapply( unlist(MI) , function(x) '$'( x , "text"))

    
    # how many tweets of each keyword
    nd = c(length(KKR_txt), length(MI_txt))

    # join texts
   # Kejriwal_txt= c(Kejriwal_txt, Kejriwal_txt2)
   # bedi_txt= c(bedi_txt, bedi_txt2)


    # Remove the duplicated tweets
    KKR_txt <- KKR_txt[!duplicated(KKR_txt)]
    MI_txt <- MI_txt[!duplicated(MI_txt)]

    # how many unique tweets of each keyword
    nd1 = c(length(KKR_txt), length(MI_txt))
    nd1

    # clean text function
    clean.text <- function(some_txt)
    {  some_txt = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", "", some_txt)
       some_txt = gsub("@\\w+", "", some_txt)
       some_txt = gsub("[[:punct:]]", "", some_txt)
       some_txt = gsub("[[:digit:]]", "", some_txt)
       some_txt = gsub("http\\w+", "", some_txt)
       some_txt = gsub("[ \t]{2,}", "", some_txt)
       some_txt = gsub("^\\s+|\\s+$", "", some_txt)
    # Remove non-english characters
       some_txt = gsub("[^\x20-\x7E]", "", some_txt)

       # define "tolower error handling" function
       try.tolower = function(x)
       {  y = NA
          try_error = tryCatch(tolower(x), error=function(e) e)
          if (!inherits(try_error, "error"))
          y = tolower(x)
          return(y)
       }

       some_txt = sapply(some_txt, try.tolower)
       some_txt = some_txt[some_txt != ""]
       names(some_txt) = NULL
       return(some_txt)}

    # clean text
    KKR_clean = clean.text(KKR_txt)
    MI_clean = clean.text(MI_txt)

    # join cleaned texts in a single vector
    KKRs = paste(KKR_clean, collapse=" ")
    MIs = paste(MI_clean, collapse=" ")
    KKR_MI = c(KKRs, MIs)

    # Corpus
    km_corpus = Corpus(VectorSource(KKR_MI))

summary(km_corpus)

    "delhiwithmodi","modipmbedicm"

    # remove stopwords
    skipwords = c(stopwords("english"),"ipl","amp","iplfantasy","match","teams", "iplopeningceremony","kxip","srh","kkr","mi","kkrvsmi",
    "opening","kolkata","mumbai","league","code", "join", "tomorrow","win", "team", "best", "support", "always",
    "pepsiipl","iplpepsi","busty","xxx","porn","boobs","open","ready","declared","jobs","face","time","iplpepsiipl","csk","rcb","watch","just","indians","jobsu","wait",
    "new","trophy","twitter","home","tour","season","performance","supporting","checking","good","cheer","gomore","crickets","listing","DD","CSK",
    "gigs","good","will","cskvsdd","ddvscsk","pepsiiplonhotstar","hashflags","gigsu","will","says","ddwhats","back","year","mirealestate","like","detroit","ceremony","see","now","get","check","day","news","way","give","cant","one","cricket","buyer","last","dont","please","can","live","see","game","job","rain","big")

    km.tf <- list(weighting = weightTf, stopwords  = skipwords,
                  removePunctuation = TRUE,
                  tolower = TRUE,
                  minWordLength = 4,
                  removeNumbers = TRUE, stripWhitespace = TRUE, 
                  stemDocument= TRUE)

    # term-document matrix
    tdm = TermDocumentMatrix(km_corpus, control = km.tf)

    # convert as matrix
    tdm = as.matrix(tdm)

    # get word counts in decreasing order
    word_freqs = sort(rowSums(tdm), decreasing=TRUE) 

    # create a data frame with words and their frequencies
    dm = data.frame(word=names(word_freqs), freq=word_freqs)

    p <- ggplot(subset(dm, freq>20), aes(word, freq))
    p <-p+ geom_bar(stat="identity")
    p <-p+ theme(axis.text.x=element_text(angle=45, hjust=1))

    png("hist.png", 480,480)
    p
    dev.off()

    dev.new()

    wordcloud(dm$word, dm$freq, random.order=FALSE, colors=brewer.pal(6, "Dark2"),min.freq=10, scale=c(4,.2),rot.per=.15,max.words=80)

    # add column names
    colnames(tdm) = c("DD","CSK")

    #write.csv(tdm,"matrix.csv")

    # comparison cloud
    png(file="CSKvsDD.png",height=600,width=800)
    par(mfrow=c(1,2))

    comparison.cloud(tdm, random.order=FALSE, colors = c("#00B2FF", "red", "#FF0099", "#6600CC"),title.size=1.5, max.words=100, scale=c(4,.2),rot.per=.15)

    # commanility cloud
    png(file="Common.png",height=600,width=1200)
    par(mfrow=c(1,2))

    wordcloud(tdm, random.order=FALSE, colors = brewer.pal(8, "Dark2"),title.size=1.5, max.words=100)

    #Sentiment Analysis code starts from here
    # run model
    mi_class_emo = classify_emotion(MI_clean, algorithm="bayes", prior=1.0)

    # Fetch emotion category best_fit for our analysis purposes, visitors to this tutorials are encouraged to play around with other classifications as well.
    emotion = mi_class_emo[,7]

    # Replace NA’s (if any, generated during classification process) by word “unknown”
    emotion[is.na(emotion)] = "unknown"

    # Polarity Classification
    mi_class_pol = classify_polarity(MI_clean, algorithm="bayes")

    # we will fetch polarity category best_fit for our analysis purposes, and as usual, visitors to this tutorials are encouraged to play around with other classifications as well
    polarity = mi_class_pol[,4]

    # Let us now create a data frame with the above results obtained and rearrange data for plotting purposes
    # creating data frame using emotion category and polarity results earlier obtained

    sentiment_dataframe = data.frame(text=MI_clean, emotion=emotion, polarity=polarity, stringsAsFactors=FALSE)

    # rearrange data inside the frame by sorting it
    sentiment_dataframe = within(sentiment_dataframe, emotion <- factor(emotion, levels=names(sort(table(emotion), decreasing=TRUE))))

    write.csv(sentiment_dataframe,"BJP.csv")

    sentiment_dataframe=read.csv("BJP.csv")

    # In the next step we will plot the obtained results (in data frame)

    # First let us plot the distribution of emotions according to emotion categories
    # We will use ggplot function from ggplot2 Package (for more look at the help on ggplot) and RColorBrewer Package

    ggplot(sentiment_dataframe, aes(x=emotion)) + geom_bar(aes(y=..count.., fill=emotion)) +
    scale_fill_brewer(palette="Dark2") + ggtitle('Sentiment Analysis of Tweets on Twitter about BJP') +
    theme(legend.position='right') + ylab('Number of Tweets') + xlab('Emotion Categories')

    ggplot(sentiment_dataframe, aes(x=polarity))+geom_bar(aes(y=..count.., fill=polarity)) +
    scale_fill_brewer(palette="RdGy") + ggtitle('Sentiment Analysis of Tweets on Twitter about BJP') +
    theme(legend.position='right') + ylab('Number of Tweets') + xlab('Polarity Categories')

    #Sentiment Analysis - AAM ADMI PARTY
    # run model

    KKR_class_emo = classify_emotion(KKR_clean, algorithm="bayes", prior=1.0)

    # Fetch emotion category best_fit for our analysis purposes, visitors to this tutorials are encouraged to play around with other classifications as well.
    emotion1 = KKR_class_emo[,7]

    # Replace NA’s (if any, generated during classification process) by word “unknown”
    emotion1[is.na(emotion1)] = "unknown"

    # Similar to above, we will classify polarity in the text
    # This process will classify the text data into four categories (pos – The absolute log likelihood of the document expressing a positive sentiment, neg – The absolute log likelihood of the document expressing a negative sentimen, pos/neg  – The ratio of absolute log likelihoods between positive and negative sentiment scores where a score of 1 indicates a neutral sentiment, less than 1 indicates a negative sentiment, and greater than 1 indicates a positive sentiment; AND best_fit – The most likely sentiment category (e.g. positive, negative, neutral) for the given text)

    KKR_class_pol = classify_polarity(KKR_clean, algorithm="bayes")

    # we will fetch polarity category best_fit for our analysis purposes, and as usual, visitors to this tutorials are encouraged to play around with other classifications as well
    polarity1 = KKR_class_pol[,4]

    # Let us now create a data frame with the above results obtained and rearrange data for plotting purposes
    # creating data frame using emotion category and polarity results earlier obtained

    sentiment_dataframe = data.frame(text=KKR_clean, emotion=emotion1, polarity=polarity1, stringsAsFactors=FALSE)

    # rearrange data inside the frame by sorting it
    sentiment_dataframe = within(sentiment_dataframe, emotion1 <- factor(emotion1, levels=names(sort(table(emotion1), decreasing=TRUE))))

    # In the next step we will plot the obtained results (in data frame)

    # First let us plot the distribution of emotions according to emotion categories
    # We will use ggplot function from ggplot2 Package (for more look at the help on ggplot) and RColorBrewer Package

    ggplot(sentiment_dataframe, aes(x=emotion1)) + geom_bar(aes(y=..count.., fill=emotion1)) +
    scale_fill_brewer(palette="Dark2") +
    ggtitle('Sentiment Analysis of Tweets on Twitter about AAP') +
    theme(legend.position='right') + ylab('Number of Tweets') + xlab('Emotion Categories')

    write.csv(sentiment_dataframe,"AAP_Data.csv")

    sentiment_dataframe  = read.csv("BJP.csv")

    ggplot(sentiment_dataframe, aes(x=factor(polarity), fill=Candidate)) + geom_bar(position="dodge")+
    scale_fill_brewer(palette="Dark2") +
    ggtitle('Sentiment Analysis of Tweets - BJP vs AAP') +
    theme(legend.position='right') + ylab('Number of Tweets') + xlab('Sentiments')

    ggplot(sentiment_dataframe, aes(x=factor(emotion), fill=Candidate)) + geom_bar(position="dodge")+
    scale_fill_brewer(palette="Dark2") +
    ggtitle('Sentiment Analysis of Tweets - BJP vs AAP') +
    theme(legend.position='right') + ylab('Number of Tweets') + xlab('Emotional Categories')
