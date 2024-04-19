# Peer-to-peer Book Exchange Platform 

The Propose P2P book exchange platform provides a global community of book enthusiasts with the opportunity to discover new books and engage in book exchanges with individuals worldwide.

At its core, the platform facilitates a seamless user experience starting with sign-up, where users can create accounts and list the books they are willing to trade. Once a book is listed, any registered user has the ability to send a request for a trade.

Upon receiving trade requests, registered users have the autonomy to review them and make decisions based on their preferences. They can choose to accept or reject trade requests, enabling a personalized and flexible trading experience tailored to individual needs and preferences.


## Target Audience and Target Market 

The target audience for the platform comprises individuals who share a passion for reading and possess a collection of books they no longer require. These individuals span diverse backgrounds and demographics, making the market reach incredibly broad.

The target audience is comprised of avid readers who are eager to exchange their surplus books for new titles that pique their interest. Whether they are students, professionals, or retirees, the platform offers an appealing opportunity to refresh their reading collection without additional expense.

Primarily, the target market encompasses individuals from middle to low-income brackets. The concept of exchanging books they have already enjoyed for new ones aligns well with their desire for cost-effective entertainment and intellectual enrichment. This demographic finds the prospect of swapping books particularly enticing, as it allows them to access a variety of reading material without straining their budget

## Propose Idea

The platform's core features should be designed with the target audience and market in mind, ensuring that its functionality and purpose resonate effectively with them.

Users should be able to easily list any books they no longer require and explore a wide range of listed books from other users. Additionally, the platform should facilitate seamless communication by allowing users to send trade requests for books that pique their interest.

Each listing on the platform should provide comprehensive information about the listed book to ensure that users have a clear understanding of its content. This information should include the book title, a summary providing an overview of the book's plot or content, the author's name, the publisher, and the year of ownership.

In addition, users should have the flexibility to edit the details of their listed books if they make any errors during the initial listing process. This user-friendly feature ensures that users can easily correct any mistakes and maintain accurate information about their listed books.

To further engage the target audience and incentivize book exchanges, the platform should incorporate a rewarding system. This system would encourage users to actively participate in trading books, thereby fostering a vibrant community and sustaining a healthy flow of traffic on the web application.

Furthermore, the platform should offer a personalized account section where users can manage their listed books and track their rewards. Additionally, comprehensive information about the platform's mission and functionalities should be readily available to newcomers, ensuring clarity and understanding of the platform's concept.

## Project Implementation (Tools and Technology)

The proposed project will be developed as a web application using the Django framework, renowned for its simplicity and effectiveness in designing web applications. Django offers built-in features such as authentication, facilitating seamless user login and authentication processes.

Additionally, Django's flexibility allows for easy integration of external APIs and front-end frameworks. For this project, we plan to leverage the Cloudinary API for storing images in the cloud and Bootstrap 5 for its simplistic and aesthetically pleasing UI components.

The web application will feature a user-friendly navigation bar on each page, enabling seamless navigation throughout the site. The webpage will be organized into several sections:

1. Home: The landing page, providing an overview of the platform and its features.
2. Listing Detail: Pages displaying detailed information about individual book listings.
3. Search: A search functionality allowing users to find specific books or listings.
4. List a Book: A form or interface for users to list their books for exchange.
5. Info: Information about the platform's mission, functionalities, and policies.
6. User Sign In/Up or User Profile: Pages for user authentication, registration, and profile management.

The home section serves as a comprehensive display of all available listings on the platform. Users, whether registered or not, can freely browse through the listings, fostering interest among non-users and encouraging engagement.

In the listing detail section, users can access specific information about each listed book by clicking on its image from the home section. Here, they can explore details of the book and express interest in trading by clicking the "request trade" button. Registered users can then confirm their interest by submitting a form, which notifies the owner of the listed book. Non-registered users will be prompted to sign up before requesting a trade. For users who have listed their own books, options to edit or delete the listing are available in this section. Deleting a listing will also remove any pending trade requests associated with it.

The search section enables users to efficiently filter and search for specific listed books based on their preferences.

The "List a Book" section provides a form for users to submit their own books for listing. The form collects essential information about the book, and users can upload multiple images for better representation.

In the info section, users can access the "about" page, which promotes and communicates the core ideas of the platform. 

The "contact" section allows users to reach out to the platform administrators in case of any issues or queries.

For non-registered or logged-out users, the User sign in/up section is prominently displayed, allowing them to either sign up or sign in. Once logged in, users can access their profile section, which includes various features:

- My Listings: Displays the user's listed books for easy editing or deletion.
- Trade Requests: Allows users to view incoming trade requests for their listed books.
- My Rewards: Enables users to track their accumulated points and view available rewards for trade.

## Core Features

- Book Listing Platform: A platform where users can easily share their unwanted books by listing them for potential trades.
- Request for Trading: Registered users can express their interest in trading by sending requests to other users for their listed books.
- Login Authentication: Robust user authentication system ensuring privacy and security of user information.
- Detailed Listings: Each listed book includes comprehensive information to help users make informed decisions before initiating a trade request.
- Simple Editing/Deleting: Users have the flexibility to edit or delete their listed books at any time, enhancing control and accuracy over their listings.
- Rewards System: Users can track their accumulated rewards points and redeem them for various reward items available on the platform.
- Aesthetic UI/UX: User-friendly interface designed to cater to book enthusiasts of all ages, ensuring an enjoyable and intuitive browsing experience.

## Future plans & idea

As the platform is still in its developmental phase, several features remain in a raw state and require further testing to enhance functionality. For instance, the request system is undergoing development, and the implementation of the search functionality is pending.

In addition to refining existing features, future development should focus on incorporating extensions to enrich user experience and engagement. Some potential features and extensions that could significantly enhance user enjoyment include:

1. Report System: Implementing a reporting mechanism to address issues such as inappropriate content or user behavior, ensuring a safe and respectful environment for all users.

2. Simple Chat System: Introducing a basic chat system to facilitate communication between users regarding potential trades or inquiries about listed books.

3. Comment Section for Each Listed Book: Adding a comment section to enable users to leave feedback or reviews on specific books, fostering community interaction and providing valuable insights for other users.

4. User Rating: Introducing a user rating system to recognize and reward trustworthy and reliable users, enhancing transparency and credibility within the community.

5. Forum Board: Creating a forum board where users can discuss various book-related topics, share recommendations, and engage in conversations with like-minded individuals, fostering a sense of community and camaraderie.

## How to Run 

To run the Web Application 

1. Clone or pull the latest version of the web application from the GitHub repository on desktop.
2. Ensure the virtual environment and dependencies are present, else install dependencies through requirements.txt 
 - pip install -r requirements.txt
3. Activate the virtual environment if it's not already activated.
4. Go into the bookExchange folder directory, and make sure that the **manage.py** file is within it
5. Apply Migrations: Ensure that the web application's database is up to date by applying migrations. Run the  following commands:
 - python manage.py makemigrations
 - python manage.py migrate
6. Verify if there are any issues or errors in the web application by running:
 - python manage.py check
7. Start the development server by executing the following command:
 - python manage.py runserver
8. Go to http://127.0.0.1:8000/discover/ , ensure */discover* is added as the end