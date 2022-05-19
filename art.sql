
CREATE TABLE "Artist" (
	"username" CHAR(20) NOT NULL,
	"firstName" CHAR(20) NOT NULL,
	"lastName" CHAR(20) NOT NULL,
	"phoneNumber" integer UNIQUE NOT NULL,
	"Email" VARCHAR2(255) UNIQUE NOT NULL,
	constraint ARTIST_PK PRIMARY KEY ("username")
	);

CREATE TABLE  "Customer" (
	"username" CHAR(20) NOT NULL,
	"firstName" CHAR(20) NOT NULL,
	"lastName" CHAR(20) NOT NULL,
	"birthDay" Varchar(20) NOT NULL,
	"phoneNumber" integer UNIQUE NOT NULL,
	"Email" VARCHAR2(255) UNIQUE NOT NULL,
	constraint CUSTOMER_PK PRIMARY KEY ("username"));


CREATE TABLE "Exhibitions" (
	"exhibitionID" INT NOT NULL,
	"artistName" CHAR(20) NOT NULL,
	"exposName" CHAR(20) NOT NULL,
	"location" CHAR(20) NOT NULL,
	"ticketPrice" INT NOT NULL,
	"startDate" varchar(255) NOT NULL,
	"endDate" varchar(255) NOT NULL,
	"openTime" CHAR(20) NOT NULL,
	"closeTime" CHAR(20) NOT NULL,
constraint EXHIBITIONS_PK PRIMARY KEY ("exhibitionID"));


CREATE TABLE "Artworks" (
	"artID" INT NOT NULL,
	"artistName" CHAR(20) NOT NULL,
	"artworkName" varchar2(255) NOT NULL,
	"information" VARCHAR2(255) NOT NULL,
	"price" INT NOT NULL,
	constraint ARTWORKS_PK PRIMARY KEY ("artID"));


CREATE TABLE "artworkPayment" (
	"paymentID" INT NOT NULL,
	"username" CHAR(20) NOT NULL,
	"artworkID" INT NOT NULL,
	"nameOnCard" CHAR(20) NOT NULL,
	"cardNumber" INT NOT NULL,
	"expiryDate" varchar(20) NOT NULL,
	"CVV" INT NOT NULL,
	constraint ARTWORKPAYMENT_PK PRIMARY KEY ("paymentID"));




CREATE TABLE "likes" (
	"artID" INT NOT NULL,
	"likesNo." INT NOT NULL);


CREATE TABLE "reviews" (
	"username" CHAR(20) NOT NULL,
	"artID" INT NOT NULL,
	"review" VARCHAR2(255) NOT NULL);



CREATE TABLE "exhibitionsPayment" (
	"exposPaymentID" INT NOT NULL,
	"username" CHAR(20) NOT NULL,
	"exhibitionID" INT NOT NULL,
	"nameOnCard" CHAR(20) NOT NULL,
	"cardNumber" INT NOT NULL,
	"expiryDate" varchar(20) NOT NULL,
	"CVV" INT NOT NULL,
	constraint EXHIBITIONSPAYMENT_PK PRIMARY KEY ("exposPaymentID"));


CREATE TABLE "Painting" (
	"artID" INT NOT NULL,
	"type" VARCHAR(20) NOT NULL,
	"style" VARCHAR(20) NOT NULL);



CREATE TABLE "Photography" (
	"artID" INT NOT NULL,
	"width" INT NOT NULL,
	"length" INT NOT NULL);



ALTER TABLE "Exhibitions" ADD CONSTRAINT "Exhibitions_fk0" FOREIGN KEY ("artistName") REFERENCES "Artist"("username");

ALTER TABLE "Artworks" ADD CONSTRAINT "Artworks_fk0" FOREIGN KEY ("artistName") REFERENCES "Artist"("username");

ALTER TABLE "artworkPayment" ADD CONSTRAINT "artworkPayment_fk0" FOREIGN KEY ("username") REFERENCES "Customer"("username");
ALTER TABLE "artworkPayment" ADD CONSTRAINT "artworkPayment_fk1" FOREIGN KEY ("artworkID") REFERENCES "Artworks"("artID");

ALTER TABLE "likes" ADD CONSTRAINT "likes_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "reviews" ADD CONSTRAINT "reviews_fk0" FOREIGN KEY ("username") REFERENCES "Customer"("username");
ALTER TABLE "reviews" ADD CONSTRAINT "reviews_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "Painting" ADD CONSTRAINT "Painting_fk0" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "Photography" ADD CONSTRAINT "Photography_fk0" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "likes" ADD CONSTRAINT "likes_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");
ALTER TABLE "likes" ADD CONSTRAINT "likes_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");
