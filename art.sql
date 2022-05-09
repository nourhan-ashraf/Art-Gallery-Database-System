
CREATE TABLE "Artist" (
	"username" CHAR(20) NOT NULL,
	"firstName" CHAR(20) NOT NULL,
	"lastName" CHAR(20) NOT NULL,
	"phoneNumber" NUMBER UNIQUE NOT NULL,
	"Email" VARCHAR2(255) UNIQUE NOT NULL,
	constraint ARTIST_PK PRIMARY KEY ("username")
	)


CREATE TABLE EXISTS "Customer" (
	"username" CHAR(20) NOT NULL,
	"firstName" CHAR(20) NOT NULL,
	"lastName" CHAR(20) NOT NULL,
	"birthDay" DATE NOT NULL,
	"phoneNumber" NUMBER UNIQUE NOT NULL,
	"Email" VARCHAR2(255) UNIQUE NOT NULL,
	constraint CUSTOMER_PK PRIMARY KEY ("username"));


CREATE TABLE "Exhibitions" (
	"exhibitionID" NUMBER NOT NULL,
	"artistName" CHAR(20) NOT NULL,
	"exposName" CHAR(20) NOT NULL,
	"location" CHAR(20) NOT NULL,
	"ticketPrice" INT NOT NULL,
	"startDate" DATE NOT NULL,
	"endDate" DATE NOT NULL,
	"openTime" CHAR(20) NOT NULL,
	"closeTime" CHAR(20) NOT NULL,
constraint EXHIBITIONS_PK PRIMARY KEY ("exhibitionID"));


CREATE TABLE "Artworks" (
	"artID" NUMBER NOT NULL,
	"artistName" CHAR(20) NOT NULL,
	"artworkName" CHAR(20) NOT NULL,
	"information" VARCHAR2(255) NOT NULL,
	"price" INT NOT NULL,
	constraint ARTWORKS_PK PRIMARY KEY ("artID"));


CREATE TABLE "artworkPayment" (
	"paymentID" NUMBER NOT NULL,
	"username" CHAR(20) NOT NULL,
	"artworkID" NUMBER NOT NULL,
	"nameOnCard" CHAR(20) NOT NULL,
	"cardNumber" INT NOT NULL,
	"expiryDate" DATE NOT NULL,
	"CVV" INT NOT NULL,
	constraint ARTWORKPAYMENT_PK PRIMARY KEY ("paymentID"));




CREATE TABLE "likes" (
	"artID" NUMBER NOT NULL,
	"likesNo." NUMBER NOT NULL);


CREATE TABLE "reviews" (
	"username" CHAR(20) NOT NULL,
	"artID" NUMBER NOT NULL,
	"review" VARCHAR2(255) NOT NULL);



CREATE TABLE "exhibitionsPayment" (
	"exposPaymentID" NUMBER UNIQUE NOT NULL,
	"username" NUMBER NOT NULL,
	"exhibitionID" NUMBER NOT NULL,
	"nameOnCard" CHAR(20) NOT NULL,
	"cardNumber" INT NOT NULL,
	"expiryDate" DATE NOT NULL,
	"CVV" INT NOT NULL,
	constraint EXHIBITIONSPAYMENT_PK PRIMARY KEY ("exposPaymentID"));



ALTER TABLE "Exhibitions" ADD CONSTRAINT "Exhibitions_fk0" FOREIGN KEY ("artistName") REFERENCES "Artist"("username");

ALTER TABLE "Artworks" ADD CONSTRAINT "Artworks_fk0" FOREIGN KEY ("artistName") REFERENCES "Artist"("username");

ALTER TABLE "artworkPayment" ADD CONSTRAINT "artworkPayment_fk0" FOREIGN KEY ("username") REFERENCES "Customer"("username");
ALTER TABLE "artworkPayment" ADD CONSTRAINT "artworkPayment_fk1" FOREIGN KEY ("artworkID") REFERENCES "Artworks"("artID");

ALTER TABLE "artist's_artwort" ADD CONSTRAINT "artist's_artwort_fk0" FOREIGN KEY ("username") REFERENCES "Artist"("username");
ALTER TABLE "artist's_artwort" ADD CONSTRAINT "artist's_artwort_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "likes" ADD CONSTRAINT "likes_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "reviews" ADD CONSTRAINT "reviews_fk0" FOREIGN KEY ("username") REFERENCES "Customer"("username");
ALTER TABLE "reviews" ADD CONSTRAINT "reviews_fk1" FOREIGN KEY ("artID") REFERENCES "Artworks"("artID");

ALTER TABLE "exhibitionsPayment" ADD CONSTRAINT "exhibitionsPayment_fk0" FOREIGN KEY ("username") REFERENCES "Customer"("username");
ALTER TABLE "exhibitionsPayment" ADD CONSTRAINT "exhibitionsPayment_fk1" FOREIGN KEY ("exhibitionID") REFERENCES "Exhibitions"("exhibitionID");

