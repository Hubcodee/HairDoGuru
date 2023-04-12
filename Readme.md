\documentclass[12]{article}
\usepackage[utf8x]{inputenc}
\usepackage{graphicx}

\begin{document}
\setlength{\parindent}{0pt}
\title{\begin{center}
    \Huge{Documentation of}
\end{center}
\begin{center}
    \Huge{\textbf{Hair-Style Recommendation System}}
\end{center}
}
\author{\LARGE{\textbf{Ansh Shrivas} (2022DS18)}\\ \LARGE{\textbf{Nitin Das} (2022CS15)} \\ \LARGE{\textbf{Ankit Kekre} (2022DS01)}}
\date{
\includegraphics[height=4.0cm,width=3.5cm]{mnnit.png}
\vspace*{0.5cm}
\\\Large{Department of Computer Science and Engineering,\\
\vspace*{0.3cm}
Motilal Nehru National Institute of Technology Allahabad, Prayagraj - 211004, India}\\
\vspace*{0.3cm}
March 27, 2023}

\maketitle

\newpage
\tableofcontents
\newpage
\section{Abstract}

The 20 Billion dollar hair care industry has the opportunity to evolve and differentiate to meet the needs of today’s high-tech, on-the-move users. Hair salons that appeal to these users must satisfy them by offering a differentiating level of service. With this project, we have attempted to address this challenge by developing a hairstyle recommendation system that identifies the user’s face shape and recommends the most flattering hairstyle that celebrities with similar face shape have used.
\vspace*{0.5cm}
\section{Introduction}
 
Choosing the perfect hairstyle can be a daunting task, but with our system, uses can find the ideal hairstyle that suits their face shape, hair texture, and personal style. Our recommendation system utilizes advanced algorithms, Machine Learning and Artificial Intelligence to analyze the user's facial features and provide them with personalized hairstyle recommendations.

Whether the user is looking for a new look, a style for a special occasion, or simply seeking some inspiration, our system can help the user to decide the best hair-style for them. Our database features a vast array of hairstyle options, including trendy cuts, classic styles, and everything in between.

With our easy-to-use interface, a user can simple click and upload a photo and receive personalized recommendations within minutes. Plus, our system also provides helpful tips and tricks for styling and maintaining the new cut.

Say goodbye to bad hair-styles and say hello to fabulous hair-styles with our Hair-Style Recommendation System!

\vspace*{0.5cm}
\section{Intended Audience}
The intended audience for our Hairstyle Recommendation System is anyone who is interested in finding a new hairstyle that suits their individual needs and preferences. This includes individuals of all ages, genders, and backgrounds who are looking for inspiration, guidance, and personalized recommendations for their hair.

Our system can be especially useful for people who are unsure about what hairstyle would look best on them, or who are looking for a change but are not sure where to start. It can also be helpful for those who may not have access to professional hair-styling services or who prefer to experiment with new looks on their own.

Overall, our Hairstyle Recommendation System is designed to be user-friendly and accessible to a wide range of individuals who are interested in exploring new hairstyle options.

\vspace*{0.5cm}
\section{Project Scope}
The scope of our Hairstyle Recommendation System is to provide personalized hairstyle recommendations to users based on their facial features, hair texture, and personal style. The system utilizes advanced algorithms and artificial intelligence to analyze user inputs and face shape to provide suggestions for hairstyles that are most likely suited to their individual needs and preferences.

The system includes a vast database of hairstyle options, ranging from trendy and modern cuts to classic and timeless styles used by prominent celebrities. Users can upload a photo of themselves and receive personalized recommendations within minutes, along with helpful tips and tricks for styling and maintaining their new hairstyle.

While our system can be a valuable resource for individuals seeking inspiration and guidance for their hair, it does not provide professional hair styling services or recommendations for hair treatments or products. It is intended as a tool to help users make informed decisions about their hairstyle options and to provide them with a starting point for further exploration and experimentation.

Overall, the scope of our Hairstyle Recommendation System is to empower users to make informed decisions about their hair and to provide them with the ideas they need to achieve the perfect look.

\subsection{Project Perspective}
    From a project perspective, the Hair-Style Recommendation System is a web-based application that utilizes advanced algorithms and artificial intelligence to provide personalized hairstyle recommendations to users. The system is designed to be user-friendly and accessible, with an intuitive interface that allows users to upload a photo of themselves and receive recommendations within minutes.

    The system includes a vast database of hairstyle options, along with information about each style, including tips for styling and maintenance. The system is continually updated with new styles and trends to ensure that users have access to the latest and most relevant information.    

\vspace*{0.5cm}
\section{User Documentation}
User documentation is an essential aspect of our Hairstyle Recommendation System, as it provides users with the information they need to use the system effectively and make informed decisions about their hair. The following is a brief overview of the user documentation that is available for our system:

\begin{itemize}
    \item \textbf{Getting Started Guide:} This guide provides users with step-by-step instructions for using the system, including how to upload a photo, how to navigate the system, and how to view and save hairstyle recommendations.

    \item \textbf{FAQ:} The FAQ section provides answers to common questions that users may have about the system, including how the system works, how accurate the recommendations are, and how often the system is updated.

    \item \textbf{Styling and Maintenance Tips:} The system includes a section that provides users with helpful tips and tricks for styling and maintaining their new hairstyle. This includes information on products, tools, and techniques that can be used to achieve the desired look.

    \item \textbf{Glossary:} The glossary provides definitions for common hair-styling terms, helping users to better understand the information provided by the system.

    \item \textbf{Contact Information:} The contact information section provides users with a way to get in touch with our team if they have any questions, concerns, or feedback about the system.
\end{itemize}

    \vspace*{0.5cm}
    \section{Open Source Frameworks Used: PHP, SQL, Flask, Machine Learning Frameworks}		 

\begingroup
    \subsection{PHP}
	
    PHP is a server-side scripting language that is commonly used for web development. It is open-source, which means that it is freely available for anyone to use and modify, and it is also cross-platform, which means that it can run on a variety of different operating systems.

    One of the key benefits of PHP is its ease of use and flexibility. It can be embedded directly into HTML code, which allows developers to create dynamic web pages that can interact with databases and other server-side technologies. PHP also includes a wide range of built-in functions and libraries, making it easy for developers to create complex web applications without having to write a lot of code from scratch.
    \newline
    \subsection{SQL}
        SQL (Structured Query Language) is a programming language that is primarily used for managing and manipulating data in relational database management systems (RDBMS). It is used to create, modify, and delete databases, tables, and records, as well as to retrieve and analyze data from those databases.
        
        One of the key benefits of SQL is its simplicity and ease of use. SQL is a declarative language, which means that users can simply state what they want to accomplish (e.g. retrieve all the records where the sales are greater than a certain amount) without having to specify how to do it. The database management system then uses the SQL statements to generate an optimized plan for executing the query.
        
        SQL supports a wide range of commands and functions, including SELECT (used to retrieve data from one or more tables), INSERT (used to add new data to a table), UPDATE (used to modify existing data in a table), and DELETE (used to remove data from a table). SQL also includes functions for grouping, filtering, and sorting data, as well as for performing calculations and aggregations.
        
    \subsection {Flask}
        Flask is a micro web framework for Python that is used for building web applications. Flask is designed to be lightweight, flexible, and easy to use, making it a popular choice for developers who want to quickly create simple web applications.

        One of the key benefits of Flask is its simplicity and ease of use. Flask has a minimalist design and only includes the essential features needed for building web applications, such as routing, request handling, and template rendering. This makes it easy for developers to get started with Flask, even if they have limited experience with web development.

        Flask also includes a wide range of extensions and plugins, which can be used to add additional functionality to the framework. These extensions can be used for tasks such as handling forms, working with databases, and authentication and authorization.

        Another benefit of Flask is its flexibility. Flask is not an opinionated framework, which means that it doesn't force developers to use a specific architecture or design pattern. This allows developers to build web applications in a way that makes sense for their specific use case.

    \subsection {Machine Learning Frameworks}
    Several machine learning algorithms were explored to train the model. Goal was to classify the user's face shape into one of 5 categories viz. heart, oval, long/oblong, round and square. Recommendation can then be given using the detected face shape.
    
    Several machine learning frameworks in python were used to build the Hair-Style Recommendation System, including:
        \begin{itemize}
    
        \item \textbf{PyTorch:} PyTorch is well-suited for building deep learning models that can analyze images and make recommendations based on visual features. For example, PyTorch could be used to build a convolutional neural network (CNN) that can recognize different hair styles and recommend similar styles to a user.
    
        \item \textbf{scikit-learn:} scikit-learn could be used to build machine learning models that analyze user preferences and recommend hair styles based on those preferences. For example, scikit-learn could be used to build a decision tree model that analyzes a user's responses to a survey or questionnaire and recommends hair styles based on their answers.  
    
        \item \textbf{PIL:} Python Imaging Library or PIL is the de-facto image processing package for Python language. It incorporates lightweight image processing tools that aids in editing, creating and saving images.

        \item \textbf{face recognition:} Recognize and manipulate faces from Python or from the command line. It is built using dlib‘s state-of-the-art face recognition and deep learning. This also provides a simple face recognition command line tool that lets the user do face recognition on a folder of images from the command line.
    
        \end{itemize}

    Additionally several machine learning techniques were explored in an attempt to train a model for this project. Some of them are discussed below.

    \begin{itemize}
        \item \textbf{K-Nearest Neighbors Algorithm:} The k-nearest neighbors algorithm, also known as k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point. While it can be used for either regression or classification problems, it is typically used as a classification algorithm, working off the assumption that similar points can be found near one another.

        \item \textbf{Random Forest Algorithm:} Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. It can be used for both Classification and Regression problems in ML. It is based on the concept of ensemble learning, which is a process of combining multiple classifiers to solve a complex problem and to improve the performance of the model.

        \item \textbf{Linear Discriminant Analysis (LDA):} Linear Discriminant Analysis (LDA) is one of the commonly used dimensionality reduction techniques in machine learning to solve more than two-class classification problems. It is also known as Normal Discriminant Analysis (NDA) or Discriminant Function Analysis (DFA).

        \item \textbf{Multilayer Perceptron (MLP):} Multi-layer perception or MLP is a feed-forward Neural Network with atleast three layers (input, hidden and output layers). Usually it has multiple hidden layers. It is a combinations of fully connected dense layers, which transform any input dimension to the desired dimension. A multi-layer perception is a neural network that has multiple layers. To create a neural network we combine neurons together so that the outputs of some neurons are inputs of other neurons.
    \end{itemize}

    Among all these models, MLP gave the best results and hence it was used in the project.
        
\vspace*{0.5cm}
\section{Roles}
    
    \textbf{Ansh Shrivas}
    \begin{itemize}
        \item Verifying that the system is processing data accurately and providing accurate recommendations to users.
        
        \item Reviewing any machine learning models used by the system to ensure that they are producing accurate and unbiased results.
        
        \item Evaluating the performance of the trained model and iteratively refining the model until it meets the desired performance standards.
        
        \item Validating the trained model to ensure that it is free of biases and providing accurate recommendations to users.
        
        \item Implementing the trained model into the hair style recommendation system and ensuring that it integrates seamlessly with the system.
    \end{itemize}

    \textbf{Nitin Das} 
    \begin{itemize}
        \item Responsible for developing and maintaining the user interface and front-end of our web-based application, as well as managing the databases that underlie the application.
        \item Verifying that the web application is responsive and provides an optimal user experience on different devices, including desktops, tablets, and mobile phones.
        \item Reviewing the source code to ensure that it follows best practices and is free of vulnerabilities.
    \end{itemize}
 
    \textbf{Ankit Kekre}
    \begin{itemize}
        \item Focused mainly on the development and training of the model and recommender code which suggests images with appropriate hair-styles based on detected face shape.
        \item Gathering and cleaning the data i.e. multiple images of famous celebrities used to train the model.
        \item Selecting the appropriate machine learning algorithm to use for the hair style recommendation system, based on the available data and the project requirements.
        \item Tuning the hyperparameters of the selected algorithm to optimize its performance.
        \item Training the machine learning model using the selected algorithm and the cleaned data.
    \end{itemize}

 \section{Security Threat}
   As a group, we tried to explore all security threats and found some threats which should not be there in any Recommendation Model.
   
   \begin{itemize}
        \item \textbf{Data privacy:}  The system may collect and store user data, including personal information such as name, email address, and hair type. This information could be vulnerable to theft or misuse if the system does not have proper security measures in place to protect the data.

        \item \textbf{Adversarial attacks:}  Adversarial attacks refer to the manipulation of input data to the model in a way that causes it to misclassify the data. Attackers can use this technique to bypass security measures or gain unauthorized access to sensitive information.
   \end{itemize}
   
\vspace*{0.5cm}
\section{External Interface Requirements}
\subsection{User Interfaces}
\begin{itemize}
    \item User can login and capture photo from camera and get recommendations based on model training data.
    \item User can view the recent recommendations based on his/her face shape
\end{itemize}
\subsection{Hardware Interfaces}
\begin{itemize}
    \item Operating system: Windows
    \item Hard-disk: 40 GB
    \item RAM: 2 GB
    \item Processor: INTEL i3 CPU
\end{itemize}
\subsection{Software Interfaces}
\begin{itemize}
    \item Visual Studio Code
    \item Postman
    \item XAMPP
\end{itemize}
%\section
%\includegraphics[height=6cm,width=6cm]{logo.jpg}
\newpage

\section{User Guide}

\begin{center}
    \begin{center}
        \textbf{Signing Up}
    \end{center}
    
    \vspace*{0.2cm}
    \includegraphics[height=7.0cm,width=10cm]{4.png}
    \newline
    \vspace*{0.5cm}
    
    \begin{center}
        \textbf{Logging in}
    \end{center}
    
    \vspace*{0.25cm}
    \includegraphics[height=7.0cm,width=10cm]{2.png}
    \newline
    \newpage
    \begin{center}
        \textbf{Capture Photo}
    \end{center}
    
    \vspace*{0.25cm}
    \includegraphics[height=8.0cm,width=10cm]{1.png}
    \newline
    \vspace*{0.5cm}
%\newpage
%\hspace*{4.0cm}
    \begin{center}
        \textbf{Recommendations}
    \end{center}
    
    \vspace*{0.25cm}
    \includegraphics[height=8.0cm,width=10cm]{3.jpeg}
    \newline
\end{center}

% \newpage
\section{Security Requirements}
\begin{itemize}
    \item System will use secured database.
    \item Normal users can just read information but they cannot edit or modify anything except their personal  and some other information.
    \item System will have different types of users and every user has access constraints
\end{itemize}
\section{Software Quality Attributes}
\begin{itemize}
   \item There may be multiple admin's creating the project ,all of them will have the right to create changes to the system.But the members or other users cannot do changes.

   \item The quality of the database is maintained in such a way so that it can be very user friendly to all the users of the database.

   \item The user be able to easily download and install the system.
\end{itemize}

\section{Business Rules}
A business rule is anything that captures and implements business policies and practices .A rule can enforce business policy,make a decision ,or infer new data from existing data.This includes the rules and regulations that the users should abide by.This includes the cost of the project and the discount offers provided .The users should avoid illegal rules and protocols .Neither admin nor members should cross the rules and regulations.

\section{Future Scope}
The future scope for a hair style recommendation system project is vast and exciting. Here are some potential areas of development:
\begin{itemize}
\item[1.] \textbf{Personalization:} The system can be further personalized based on the user's hair type, facial features, skin tone, and personal style preferences. The system can use machine learning algorithms to analyze a user's past hair styling choices, and recommend styles that fit their unique profile.

\item[2.] \textbf{Virtual Try-On:} Virtual try-on technology can be integrated into the system, allowing users to see how different hair styles will look on them before making a final decision. This will help users make more informed decisions and increase their satisfaction with the recommended styles.

\item[3.] \textbf{Partnerships with Salons and Stylists:} The system can partner with salons and stylists to provide users with more comprehensive hair care solutions. This could include access to personalized hair care products and services, as well as recommendations for stylists who specialize in the recommended hair styles.

\item[4.]  \textbf{Partnerships Hair-Transplant Clinics:} The system can partner with leading Hair-Transplant Clinics nearby and recommend a list with respective pricing to users whom the system detects having hair related problems such as hair-loss.

\item[5.] \textbf{Integration with Social Media:} The system can be integrated with social media platforms, allowing users to share their new hair styles with their friends and followers. This will help to increase the visibility of the recommendation system, and generate more interest in the product.
\end{itemize}

Overall, Hair Style Recommendation System has a plethora of applications. With continued development and integration of latest technologies, this project has the potential to completely transform the hair-care and fashion industry.

\newpage
\section {Declaration}
We, the undersigned, solemnly declare that the project report on \textbf{Hair Style Recommendation System} is based on our own work carried out during the course of Programming Lab 2  under the supervision of Prof. A.K. Singh.
We assert the statements made and conclusions drawn are an
outcome of our project. We further certify that
\begin{itemize}
\item The work contained in the report is original and has been
done by us under the supervision of Prof. A.K. Singh.
\item We have followed the guidelines provided by the instructor in writing the report.
\end{itemize}
\vspace*{5cm}
By Group - 15
\newline
\newline
\textbf{Ansh Shrivas} (2022DS18)
\newline
\textbf{Nitin Das} (2022CS15)
\newline
\textbf{Ankit Kekre} (2022DS01)

%\begin{frame}[allowframebreaks]\frametitle{References}
%% \renewcommand{\bibname}{References}
%%\nocite{*}
%\bibliography{story}{}
%\bibliographystyle{ieeetr} 
%\end{frame}

\end{document}
