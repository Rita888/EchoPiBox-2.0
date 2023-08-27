# EchoBoxPi2.0

Detect.Classify.Exhibit


<img width="398" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/ce94ce5b-daa7-4f7f-b86f-efd7c5d6ff24">


EchoPiBox 2.0 Passive Acoustic Monitor: Detection, Species Identification Accuracy and Displaying Real Time Data.

MSc Connected Environments Dissertation by Margarita Smoldareva

Research Question: Can Raspberry Pi 4 host open-source machine learning model and three additional sensors to classify social bat calls plus display environmental variables along with accurate bat species in real time using Flutter App? 

This study is part of MSc Connected Environments programme which explores the use of a microprocessor and other hardware components wired together in a box with ability to detect and classify bats using open-source machine learning model developed by University College London (UCL). The aims and objectives of this thesis report are noted below that indicated the flow of the project. 

Detect
Aim: - Build a physical device (EchoPiBox 2.0) which allows bat calls detection. 
Objective: Set up Raspberry Pi 4, Ultramic, Temperature/Humidity and GPS Sensors to record environmental variables and bat calls. 

Classify
Aim: - Deploy Machine Learning Algorithm on EchoPiBox 2.0 and test its accuracy. 
Objective: Select and deploy the device across five sites based in England and Wales to test accuracy of classification of bat calls. 

Exhibit
Aim: - Display the Real Time Data
Objective: Using Flutter App display data collected by EchoPiBox 2.0 when deployed at any time.

<img width="457" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/b0ada444-462e-40e8-a8ac-3d8e83f9fcb8">
Flowchart 1: Proposed Scheme for Deployment

UK bats and their importance 
Bat, being the sole flying mammal of the world is the most diverse specie on Earth. Except for Antarctica, they are found on every continent. 
In the United Kingdom, 18 different breeds of bat along with some vagrant visitors are found (Entwhistle et al., 2001). Bats are important creatures whose ecological 
roles as predator and prey have been postulated to regulate environmental and economic services including nutrient distribution, arthropod suppression, pollination, 
and biodiversity. For the purpose of foraging and roosting, the utilisation of different habitats by bats regulates nutrient dispersion and soil fertility to
facilitate dietary transfer within ecosystems from nutrient-rich locations to poor-nutrient regions (Buchler, 1975). Furthermore, bats serve as exceptional 
ecological indicators of habitat quality. Due to their mobility, ecological distribution, population trends, taxonomic stability, size, global distribution, 
and longevity, bats have great potential as bioindicators for contaminants and disturbance in the atmosphere (Kasso and Balakrishnan, 2013, 4). 

Similarly, tropical bats provide immense support as pollinators to national and local economies. The role of bats as a bioindicator taxa is highly essential to
evaluate climatic responses, loss of habitat, and insects’ population in a particular region enabling the researchers to reflect on forthcoming impacts and 
wider-scale changes on biodiversity.

Despite being an essential contributor to the environment and nature, bat populations have drastically declined in the United Kingdom. Due to a lack of substantial 
historical data on bat distribution and population sizes, it is hard to quantify the population decline. However, some common issues for bats' survival include poor 
management of their feeding habitats, roost sites, and lack of protection of hibernation sites (hibernacula) (Entwhistle, 7). Thus, the population of British bats
has shrunk notably and species conservation techniques and interventions are being studied and implemented to meet their habitat requirements (Hill and Greenaway, 2008).

Bat Conservation Trust (BCT, 2023) play a vital role in advocating for conservation, raising awareness, conducting research, and providing resources and guidance for 
individuals, communities, and professionals. 

Bioacoustics
Within the ecological realm, studying acoustic signals have been a renowned scientific method for investigating sound dispersion, reception, and production of different
mammals and birds (Wang and Bu, 2022, 250). To determine species abundance and bat activity, bioacoustics methods are used to extract essential information and data from
bats’ echolocation calls for conservation monitoring and biodiversity research (Ruiz et al., 2017). Bats are nocturnal mammals that utilise an echolocation system
(high-frequency calls) to picture and navigate their environment in the dark. The basic mechanism of echolocation is similar to sonar, where the returning echoes
are used to create a sonic picture of their surroundings. These ultrasonic calls are recorded and captured by ecologists to study bat activities in a certain area.
The bio sonar mechanism in bats serves as an acoustic imaging modality in real time (Simmons and Gaudette, 2012, 556). This mechanism enables bats to extract 
detailed information about their location as the auditory systems of bats are equipped with highly specialised neurons (Suga, 1990). In the life of echolocating bats,
bio-sonar provides a wide range of functionalities from finding food, navigating obstacles, and locating and flying through dangerous surroundings for example vegetation.

Acoustic detection of bat species includes recognition and observation of call patterns and design from sonograms of ultrasonic calls. However, the conventional manual 
identification of these calls requires a higher level of training and tend to be very time-consuming (Ruiz et al., 2017). The ultrasonic calls are the carriers of bats' 
information into the environment that are beneficial to explore population trends, activity patterns, specific-specie identification, and overall health of the 
environment (Gallacher et al., 2021). As per the study presented by Clement et al., (2014), the identification procedure includes a set library of calls of the target 
species, extraction of frequency and time data from call spectrograms, and lastly, the implementation of statistical technique to predict and analyze the identity of 
vocalizations captured during acoustic examination. Bioacoustics methods are noninvasive remote surveys that require less effort and hard work compared to labor-
intensive trapping and roost monitoring methods (Walters et al., 2013, 480). 

BAT DETECTORS ON THE MARKET

The utilisation of bat detectors in bat population conservation plays a crucial role to identify important foraging and roosting sites that ensure their survival. It is 
a battery-operated, handheld device that is used to capture and record ultrasonic bat calls. In the beginning, these detectors were intended as a DIY project that later 
evolved, becoming high-quality equipment for bat scientists and wildlife enthusiasts. The ultrasonic sounds produced by bats during their echolocation calls can be 
converted into audible audio with the help of a bat detector. The characteristics of these calls can be used to identify the bat species and nocturnal activities.

Song Meter Mini Bat

It is the lightest (290g), most affordable, and smallest (12.3 x 16.8 x 3.6 cm) commercially available audio recorder. It can process and record data for up to 30 nights 
(10 hours each) with 4 AA batteries. It is equipped with a built-in microphone offering identical quality to the SM4 mics. The recorder is Bluetooth enabled and the 
settings of the device can be easily accessed with the app. This detector comes equipped with a Kingston SDHC card, rechargeable batteries, and Masterlock Python Cable 
8417D (Nationwide Ecology Supplies, n.d).

Song Meter-SM4BAT-FS with SMM-U2

This particular bat detector is the most widely used full-spectrum static device that can survive in the field for a whole month with D-cell batteries. The entire 
detection system is enclosed in a polycarbonate rugged casing with weatherproof covers and mounting brackets. It has a pre-programmed schedule for effective bat surveys
and also enables customized schedules too. It has a single microphone recording channel that rates up to 16-bit 500 kHz.


MACHINE LEARNING IN BIOACOUSTICS 

BATCORDER
According to Fritsch and Bruckner (2014), a large amount of call recordings can be facilitated through software-based identification, especially for extensive acoustic
experiments that involve various collaborators. However, validation at the time of species classification may raise identification bias where more than one participant 
is present due to varying degrees of knowledge and experience. This could affect the quality of the data being analyzed, more specifically for species with difficult 
acoustic frequencies. Keeping this in view, the authors explained the working mechanism of the batcorder system where the automated classification of the species list 
can generate an unvalidated output of call sequences. The system of batcorder contains three main operable working units namely the batcorder, which is the recording 
device, bcAdmin, which is the visualization and administration software and lastly batIdent, which is the identification software. The acoustical properties during the 
survey are recorded, measured, and discerned by bcAdmin based on the minimum and maximum frequency and call length. These measurements are then transferred to batIdent 
for individual call identification. This part of the software utilizes Random Forest Algorithm for identification via R statistical software. Each call sequence is 
classified into different calls while the long sequences with many calls are further classified. Each call within the classification is assigned to more than one taxon,
resulting in unvalidated call sequences. In their study, Fritsch and Bruckner raised the concern to standardize the process of validation by harmonizing the results of
operators with different experiences. 


RANDOM FOREST ALGORITHM
In the study presented by Ruiz et al., (2017), a computational method for the automated detection and identification of bat species was proposed. Based on the 
echolocation mechanism, the authors aimed to perform an experiment in complex soundscapes of tropical ecosystems. The experiment involved a statistical voice activity
detector coupled with a supervised machine learning technique namely a random forest algorithm. The test was performed using a library of echolocation calls belonging
to 36 different species of neotropical bat. The research aimed to accurately identify and detect a diverse group of bat species within noisy and complex soundscapes 
from natural environments. Generally, to identify bat calls in ultrasonic frequency, the audio signal is represented in the range of time frequency. However, signal 
distortion (microphone gain) and background noises (including power lines, insects, electronic devices, and footsteps) are most likely to hinder signal detection from 
the area of inspection. Similarly, the authors also argued the effectiveness of spectrograms for bat call detection but ended up using VAD (voice activity detector)
technique. This technique is a model-based procedure that utilized speech processing to detect the absence or presence of speech. Also, a model-based approach for 
detection has fewer false positives compared to spectral peak detectors in spectrograms (Skowronski and Fenton, 2008). The result of the study showed that the random 
forest technique proved to be the most accurate machine learning algorithm for the acoustic identification of bat species among the five learning classifiers. 

CONVOLUTIONAL NEURAL NETWORK
Passive acoustic sensing as a way of monitoring and surveying anthropogenic impacts on wildlife and biodiversity has recently become a useful tool, specifically to 
quantify bat echolocation calls. As per the study presented by Mac Aodha et al., (2018), an open-source CNN (convolutional neural network) based pipeline was introduced
to detect search-phase, ultrasonic, and full spectrum calls generated by bats. The deep learning algorithms used by the authors were trained to collect ultrasonic audio
along road transects in Bulgaria and Romania by researchers in iBats program. The design of the CNN-based detector was tested against different commercial systems and 
algorithms on datasets recorded in different countries using varying sensors. The testing showed that the CNN-based detector has higher performance in terms of recall 
and precision of search-phase bat calls as compared to commercial systems. 

The researchers were successful to portray the automated and accurate search-phase detection of bat calls, specifically retrieved from a noisy audio recording. 
The deep learning-based pipeline allowed automatic monitoring and detection of bat species and populations. The system was further incorporated to cater to transparency
and progress for forthcoming systems. The CNN system was able to localize echolocation bat calls in recordings which was earlier a very difficult task in commercial 
systems, especially retrieving from noisy audio. 

BATDETECT2
Despite the fact that acoustic monitoring is a scalable and effective technique to assess the activities and patterns of bioindicator taxa, there exists a substantial 
amount of noise and distortion in the data. For this reason, it is important to use accurate tools that automatically detect the presence of the targeted specie.
As per Mac Aodha et al., (2022), in such scenarios, machine learning-based techniques have the maximum potential to yield optimal results, however,
to properly deploy the technique, expertise is required. In their study, the authors have proposed a novel approach for echolocation call detection 
namely BatDetect2. It is a deep learning-based pipeline that classifies and detects bat species by interpreting acoustic data. 
As per the authors, the outputs of BatDetect2 are interpretable as it allows direct indication of echolocation calls in terms of frequency and time. 
Furthermore, the temporal information from the surrounding is also utilised by BatDetect2 which maintain the computational efficiency at the time of deployment and 
improve its predictions. To enable researchers and practitioners to deploy, annotate and train the model, BatDetect2 contains open-source tools in the datasets.
The authors comprehensively tested the effectiveness of the model on five datasets, retrieved from four different geographical locations 
(Brazil, UK, Australia, and Mexico). For a 17 UK bat species dataset, the mean average was 0.88, which was visibly better than the 0.71 attained by the
conventional call extraction baseline method.


BAT POINT COUNTS
In their study, Darras et al., (2021) explored the promising results of electromagnetic energy to sample bat communities. According to the authors, the bat point counts 
technique is a novel sampling procedure that eradicates the shortcomings and sampling bias of conventional sampling techniques. The novel method involves a sampling rig
joined with a thermal scope for bat detection, a near-infrared camera for capturing the bat morphology, and an ultrasound recorder to collect echolocation calls. The 
bat point counts serve as a non-invasive, competitive, and promising novel tool that aids in observing bats’ behaviour in the environment without bias.  

RASPBERRY PI IN BIOACOUSTICS
The vast capabilities of the Raspberry Pi, including its ease of use, customisable hardware, and low cost make it a commendable research tool in the field of bat
detection and bioacoustics. Similarly, automatic recording of bat echolocation calls, vegetation structure, bat diversity, and population can be done using bat 
detectors made with Raspberry Pi technology (Jolles, 2021). For bioacoustics, Raspberry Pi is being readily used for audio recording to assess habitats, biodiversity,
and vocalizations of bats and birds. A Bioacoustics recorder named ‘SOLO’ was built by Whytock and Christie (2017), using a single board of Raspberry Pi that could 
record audio for straight 40 days being highly customizable and easy to use. Similarly, a bat survey on a derelict building in the UK was carried out using Raspberry Pi
technology and a simple ultrasonic mic (Whittaker, 2020). The system consisted of Raspberry Pi software, an ultrasonic mic, and an STM M0 processor. The recorded audio 
was sent to the software using bash language that received the data from Alsa driver software. With the help of this device, a team of bat enthusiasts was able to 
identify 9 different species of bat in the United Kingdom.

Similarly, with the use of a 384 kHz full spectrum recorder and Raspberry Pi Pico bat detector, sonic chirps of bats can be easily heard and recorded during their 
nocturnal activities (Horsey, 2023). The Pico bat detector processes the audio in real-time due to which live calls of bats’ echolocation can be heard. The time 
expansion mode in the detector is present to slow and transposed down the speed of the audio 16x and 4 octaves down respectively. Within the detector, the operational
amplifier and ultrasonic microphone are present that amplify and capture the bat calls which are sampled by Raspberry Pi. The functionality of the device resembles a 
full-spectrum recorder where 384 kHz ultrasonic audio can be saved to allow offline analysis as well. The LED display powered by Raspberry Pico’s PWM system provides an
analog display and speech synthesis feedback is present to pinpoint targeted bat calls and accurate detection of the frequency.

Bat Pi 4, a new, compact yet highly functional version of the bat detector has been introduced with an easy operational and configurational setting that is LAN enabled
and provides cloud technology that stores audio recordings for offline analysis (Raspberry Pi bat project, n.d). The recording from this detector is time-controlled 
with GPS support and an ultrasonic USB microphone to capture bat calls during their nocturnal activities.

LIGHT AND WEATHER CONDITIONS IMPACT ON BATS
With a rapid increase in the human population in urban areas, the landscape of the cities is constantly expanding posing various vicissitudes in ecosystems such as decreased habitat connectivity due to roads, buildings, and surface sealing concrete and variance in local climates (Voigt et al., 2020). All of these anthropogenic 
disturbances caused wildlife species to shift their urban habitats and environment. One of the most crucial anthropogenic stressors for bats is ALAN (artificial light
at night). Being nocturnal creatures, bats are designed to function more effectively during the nighttime. However, the physical and psychological cycle of bats is 
highly vulnerable to the adverse side effects of ALAN on their nocturnal activities. In some cases, during foraging some bats prefer ALAN sites but the majority of the 
evidence suggested that bats tend to bypass and avoid illuminated drinking sites, even foraging places and illuminated routes (Zeale et al., 2018). Voigt et al. 
analysed the spatial behavior of noctule bats with miniaturized GPS loggers to assess the habitat features of urban bats with respect to ALAN and found that the 
majority of the bats repelled and resisted flying across illuminated neighborhoods especially roads during foraging as the traffic noise was an additional repellant to
their natural habitat requirements. 

Supporting the aforementioned study, Laforge et al., (2019) presented a similar idea in their research where the authors proposed that light pollution can affect 
landscape connectivity and movements of the animals, especially in ever-evolving urban landscapes. Due to this, conservation interventions are constantly being employed
to reduce light during the night to help bats reconnect with the landscape. The authors utilized a species distribution model with random stratified sampling on Myotis 
daubentonii, Pipistrellus nathusii, and Eptesicus serotinus. The result of the study showed a positive response of light reduction for M. daubentonii and P. nathusii. 
Thus, the author recommended preventive measures for light reduction in urban planning to maintain sustainable habitat conditions for urban bats. 

Similarly, as per Cravens and Boyles (2019), the use of artificial lights in the city may induce disturbances for the wildlife community. The authors tested the 
differential impact of light pollution on insectivorous nocturnal bats using a physiological technique by measuring the blood metabolite (ß-hydroxybutyrate) of 6 
species of bats in unlit and lit conditions. Bat calls were also recorded acoustically to assess activity levels during the experiment. The results of the study 
suggested that only red bats were able to actively forage in lit conditions, while the rest of the specie avoided light. 

Apart from artificial light, weather conditions also pose alterations to bats living conditions and activities in terms of hibernation, life cycle, and prey 
availability (Mendes et al., 2017). Unfavorable weather situations like strong winds and heavy rain negatively affect bat activity. The ecological terrain selection of 
bats heavily relies on weather conditions, air temperature, and prey availability during site selection for their habitats. 

METHODOLOGY 

DETECT – BUILDING THE DEVICE 

The main component of a bat detector is a microphone which is able to detect echolocation emitted from the bats. The additional sensors provide more data which can influence bat species accuracy such as light sensitivity and location. 

<img width="125" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/107e9f74-e2b9-498c-af09-3b636da88072">
Plate 1: Ultramic (NHBS, 2023)

The Ultramic is a fully digital USB ultrasound microphone with integrated digital to analog converter and an option of 192 kHz, 200kHz or 250kHz sampling rate.
The USB 2.0 port allows for easy connection to your PC or MAC and no driver installation is required.
Compact and versatile the Ultramic is a great option for use in the field or laboratory. Whilst most often used to record the ultrasonic signals of both bats and 
rodents it is equally useful for detection of high-frequency noises emitted by LCD screens, turbines and power adaptors.

Specification
* 192K, 200K or 250K sampling per second.
* True 16 bit resolution.
* Frequency range up to 100kHz - 125kHz.
* MEMS high sensitivity Surface Mount Wide-band Ultrasonic Acoustic Sensor.
* High quality and low noise analogue amplification.
* USB full speed port with a mini B USB connector.
* 32 bit 80MHz integrated microcontroller.
* Dimensions: 130mm length x 20mm diameter.
Available on https://www.nhbs.com/ultramic-usb-ultrasound-microphone

[
](https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052740158&src=raspberrypi
https://thepihut.com/products/adafruit-aht20-temperature-humidity-sensor-breakout-board (optional)
https://thepihut.com/products/adafruit-tsl2591-high-dynamic-range-digital-light-sensor (optional) 
https://thepihut.com/products/adafruit-mini-gps-pa1010d-uart-and-i2c-stemma-qt (optional)
Micro SD of minimum 256GB is recommended (64gb or more for software back up)
)https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052740158&src=raspberrypi
https://thepihut.com/products/adafruit-aht20-temperature-humidity-sensor-breakout-board (optional)
https://thepihut.com/products/adafruit-tsl2591-high-dynamic-range-digital-light-sensor (optional) 
https://thepihut.com/products/adafruit-mini-gps-pa1010d-uart-and-i2c-stemma-qt (optional)
Micro SD of minimum 256GB is recommended (64gb or more for software back up)

<img width="351" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/364593d6-82ed-4be1-b4e1-f4be8a62e9a8">
Plate 2: Diagram of connecting the components (Solidworks, 2023)

<img width="334" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/a3b4e036-1086-448d-8f09-37fd3263d2a7">
Plate 3: Diagram of connecting the remaining  components (Solidworks, 2023)

<img width="228" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/e6efee83-4860-4a0d-9634-48d279ce69b1">
Plate 4: Connecting the wires (Fritzing, 2023)

![image](https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/50d20aac-a4be-4b2f-bf0f-ce363eed4a0a)
Plate 5: Final EchoPiBox 2.0 (EPB) Hardware Assembly (Smoldareva, 2023)

CLASSIFY – IDENTIFICATION AND TESTING ACCURACY 

To classify bat social calls, open source BatDetect2 (Macaodha, 2023 ) model was used to build up on to produce Acoupi software . 
The Acoupi software utilises the code used to run the BatDetect2 algorithm. 
Raw data produced by Acoupi software in Raspberry Pi. 

For this project, series of sites were selected to include habitat complexity that would allow different bat species to be present to test the accuracy of detecting as 
many of UK bat species at possible. The Bat Conservation Trust (BCT, 2023) provides comprehensive guidelines for conducting bat surveys, ranging from preliminary
assessment, emergence/re-entry, transect and roost surveys.

Due to personal experience of undertaking diverse bat surveys over eight years, it was possible to select sites in England and Wales with known presence of bats. 
Five sites were of diverse habitats and surrounding landscapes as described later in this chapter. The surveyor holds Natural England Level 1 Bat Licence therefore 
permitted to use artificial light to identify bat species. 

The nocturnal bat surveys commenced 20 minutes prior to sunset and completed around 90 to 120 minutes after the sunset. In conjunction to EchoPiBox 2.0, Echo Meter 
Touch (EMT) Pro for iOS from used to then compare the species recorded. The recordings were later analysed using Wildlife Acoustics Software to verify bat calls 
recorded on EMT.  

Deployment Results
<img width="476" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/fbc17e90-b4da-4888-9daf-06d04bde55d5">
<img width="453" alt="image" src="https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/e1c28a1e-2c56-41f3-952f-61c26641fdb2">


EXHIBIT – DISPLAY REAL TIME DATA ON FLUTTER APP

Once the data collected using EMT was analysed using Kaleidoscope Viewer for Bat Analysis (Wildlife Acoustics, 2023) it then compared to the data collected using 
EchoPiBox 2.0. The accuracy of the Acoupi detection was set to 60% therefore any bat calls with less than 59% would not be displayed on the app. 

![image](https://github.com/Rita888/EchoPiBox-2.0/assets/93122551/81fa4b8b-36ba-4463-b972-3b99b342b08c)
Flow chart 2: Overall Detection, Classification and Display Flow Chart

DISCUSSION AND FURTHER RECOMMENDATIONS 

BUILDING THE EPB– The aim of this study was to include the hardware that will be used to correctly identify bat species while deployed in the wild. 
The ultramic and the sensors did not present any challenges during the deployment. The power source was not discussed in this project as the main aims were to build a 
working bat detector, test the accuracy of the BatDetect2 model and display real time data using flutter app. As this device can be used as a handheld detector as well
as a static detector, therefore deployed over series of nights, weeks, months or be permanently installed on a lamppost. For this study portable DC/AC Power Bank with 
99WH capacity was used as the surveys were lasting over two hours at each of the time. If these are to be used as static detector, different power source should be used
to accommodate the power consumption of the Raspberry Pi. 

It must be also noted that the sensors were not calibrated and not tested during this study therefore further testing is recommended. Although, the real time data was 
displayed on the app, the accuracy of data particularly was lux, temp/humidity sensors were not tested due to lack of time. The GPS location was out by 25 to 50m which 
is suitable for this study however if more precise location is needed, use of another sensor is recommended. 

Also to be noted that due to 11-12 hours deployment time, the environmental data recorded was insufficient to allow any analysis of these parameters to determine 
accuracy of bat species such as the light sensitive bat species (e.g. Brown Long-eared bat and Myotis sp.) Further assessment would allow lux sensor to determine 
likelihood of bat species present within the locality. 

SETTING UP THE EPB– The software element was the most challenging in this study and about 70 per cent of the time spent on the project was to set up the Raspberry pi 
and provide the code for the sensors due to non-engineering background. Hence the detailed guid was produced to allow fellow ecologists with non-engineering background 
to navigate through EchoPiBox 2.0 set up. 

BATDETECT2/ACOUPI were easy to install once the Raspberry Pi was set up. Several deployments were undertaken prior to conducting surveys away from home. The accuracy 
was tested and concluded that any detections above 60% will be displayed on the real time data stream and anything less than 59% will be discarded. It is recommended 
that further deployments and tests are carried out to conclude on the accuracy percentage as just over ten hours of recordings cannot be sufficient to conclude on the 
accuracy. It is also recommended to deploy in different locations to capture all 17 UK species as only 11 species were classified during this study. 

The raw data shown that 14 species were recorded on one night of deployment however once the accuracy was changed to 60% this number dropped to 6 species. 
The species  might be occupying that specific location however due to only two-hour deployment; these bat species might have been too far away to be detected accurately. 

CONNECTIVITY – During the deployment, to test if the EPB is switched on, personal smart phone hotspot and TeamViewer App was used. Once the Flutter App was build, 
Alcatel 8094T Android tablet was used for hotspot connection. The device can be used in the wild without connectivity however there is a risk that the automated (PM2) 
is not running therefore not recording the data. The app allows to test if the device is operating by displaying the real time data however another way of connectivity 
must be explored to allow other sources of connection such as Long Range Wide Area Network (LoRaWAN). This will enable long range communication with low power 
consumption, allowing appliactions requires remote and battery-operated devices to transmit data over relatively long distances. 

THERMAL CONSTRAINTS – Once the device was inside its 3D printed box, the temperature emitted from the Raspberry Pi started to influence the sensor. For further design 
improvements, the temperature/humidity sensor should be placed outside the device box to avoid the false data reading. 

STORAGE – For this project 64GB SD card was used at the initial stage and by the second night of deployment, it was noted that more storage is needed. The SD was backed 
up and cloned using ApplePiBaker Software (PiBaker, 2023) on varies occasions to allow 256GB SD to be the final operation SD card installed within the Raspberry Pi 4. 

RAM – The Raspberry Pi 4 which was used for this study had 8GB which is lower than the traditional desktop or laptop computers. Although, the real time data was 
displayed on the app, there is a slight delay and at the time of the write is was inconclusive if this issue was due to RAM or Firebase/iCloud limitations. 

BETTER IOT – To make this device more sustainable, it is advised to use the assessment tool provided by the Better IOT. This tool was developed to address some of the
pressing issue in the early stages of development to include: “privacy, openness, interoperability, lifecycle, permissions, transparency, data governance and security”.
(BetterIOT, 2023). 

CONCLUSION 

This study had three aims and objectives: Detect, Classify and Exhibit, as stated at the start of this document. The physical device has all the hardware components 
needed to start recording bat calls as well as additional sensors that could impact on presence of bats such as temperature, artificial light and the location. 
To classify the bat calls collected, open-source machine learning Acoupi software (stemmed from BatDetect2 model) was installed on Raspberry Pi. 

The device was installed over 10 hours, approximately 2 hours at each of five different locations in England and Wales to detect as many bat species as possible. 
In total 11 species were recorded during deployment and the accuracy of open-source model was concluded to be precise. Due to Ultramic is very sensitive and many
misclassifications were recorded and the accuracy of the detection was then coded to 60% which reduced the species recorded from 14 to 11. 

The data collected was then sent to iCloud (Firebase) which then allowed the real time data to be displayed on the EchoPibox 2.0 Flutter App. There was a slight delay
of several seconds in displaying the data depending on its connectivity to WiFi or Mobile Hotspot. 

Overall, the study was successful however the report highlighted several improvements and recommendations in the discussion section to include power supply, calibrating
the sensors, connecting to stable data transmitting network, redesigning the enclosure box to be more robust and complaint with International Protection Rating (IPR). 
Lastly, it is also advisable to use Better IOT assessment tool to allow the device to be in line with sustainability. 



Applepi-Baker v2 for Raspberry Pi. Tweaking4All. (https://www.tweaking4all.com/software/macosx-software/applepi-baker-v2/ Accessed on 20th July 2023
Bat Conservation Trust. Guidance for professionals. (https://www.bats.org.uk/resources/guidance-for-professionals) Accessed on 10th May 2023

Better IOT. Making Good Design Actionable. (https://betteriot.wordpress.com) accessed on 25th August 2023 

Buchler, E. R. (1975). Food transit time in Myotis lucifugus Chiroptera: Vespertilionidae. Journal of Mammalogy, 56(1), 252-255.

Clement, M.J., Murray, K.L., Solick, D.I. and Gruver, J.C., 2014. The effect of call libraries and acoustic filters on the identification of bat echolocation. 
Ecology and evolution, 4(17), pp.3482-3493.

Cravens, Z.M. and Boyles, J.G., 2019. Illuminating the physiological implications of artificial light on an insectivorous bat community. Oecologia, 189, pp.69-77.

Darras, K.F.A., Yusti, E., Huang, J.C.C., Zemp, D.C., Kartono, A.P. and Wanger, T.C., 2021. Bat point counts: A novel sampling method shines light on flying bat
communities. Ecology and Evolution, 11(23), pp.17179-17190.

Entwhistle, A.C., Harris, S., Hutson, A.M., Walsh, A., Gibson, S.D., Hepburn, I. and Johnston, J., 2001. Habitat management for bats-a guide for land managers, land 
owners and their advisors.

Fritsch, G. and Bruckner, A., 2014. Operator bias in software‐aided bat call identification. Ecology and evolution, 4(13), pp.2703-2713.

Gallacher, S., Wilson, D., Fairbrass, A., Turmukhambetov, D., Firman, M., Kreitmayer, S., Mac Aodha, O., Brostow, G. and Jones, K., 2021. Shazam for bats: 
Internet of Things for continuous real‐time biodiversity monitoring. IET Smart Cities, 3(3), pp.171-183.

Hill, D. A., & Greenaway, F. (2008). Conservation of bats in British woodlands. British Wildlife, 19(3), 161.

Horsey, J. (2023, July 17). Listen to bats using the raspberry Pi Pico bat detector. Geeky Gadgets. https://www.geeky-gadgets.com/raspberry-pi-bat-detector-17-07-2023/

Jolles, J.W., 2021. Broad‐scale applications of the Raspberry Pi: A review and guide for biologists. Methods in Ecology and Evolution, 12(9), pp.1562-1579.

Kasso, M., & Balakrishnan, M. (2013). Ecological and economic importance of bats (Order Chiroptera). Isrn Biodiversity, 2013, 1-9.
Laforge, A., Pauwels, J., Faure, B., Bas, Y., Kerbiriou, C., Fonderflick, J. and Besnard, A., 2019. Reducing light pollution improves connectivity for bats in urban
landscapes. Landscape Ecology, 34, pp.793-809.

Mac Aodha, O., Gibb, R., Barlow, K.E., Browning, E., Firman, M., Freeman, R., Harder, B., Kinsey, L., Mead, G.R., Newson, S.E. and Pandourski, I., 2018. 
Bat detective—Deep learning tools for bat acoustic signal detection. PLoS computational biology, 14(3), p.e1005995.

Mac Aodha, O., Martinez Balvanera, S., Damstra, E., Cooke, M., Eichinski, P., Browning, E., Barataud, M., Boughey, K., Coles, R., Giacomini, G. 
and Mac Swiney G, M.C., 2022. Towards a General Approach for Bat Echolocation Detection and Classification. bioRxiv, pp.2022-12.

Mendes, E.S., Fonseca, C., Marques, S.F., Maia, D. and Ramos Pereira, M.J., 2017. Bat richness and activity in heterogeneous landscapes: guild-specific and scale-dependent?. Landscape ecology, 32, pp.295-311.

Nationwide Ecology Supplies. Bat Detectors. https://www.wildcare.co.uk/media/amasty/amfile/attach/r7DGJpG7YFh6ydqaKHuKLH1QFbJUxTKa.pdf (accessed on 11th August 2023)

Raspberry Pi bat project. (n.d.). Raspberry Pi Bat Projekt. https://www.bat-pi.eu/EN/index-EN.html

Ruiz, A.T., Jung, K., Tschapka, M., Schwenker, F. and Palm, G., 2017. Automated identification method for detection and classification of neotropical bats.

Simmons, J.A. and Gaudette, J.E., 2012. Biosonar echo processing by frequency-modulated bats. IET Radar, Sonar & Navigation, 6(6), pp.556-565.

Skowronski, M.D. and Fenton, M.B., 2008. Model-based automated detection of echolocation calls using the link detector. The Journal of the Acoustical Society of America, 124(1), pp.328-336.

Suga, N., 1990. Biosonar and neural computation in bats. Scientific American, 262(6), pp.60-71.

Voigt, C.C., Scholl, J.M., Bauer, J., Teige, T., Yovel, Y., Kramer-Schadt, S. and Gras, P., 2020. Movement responses of common noctule bats to the illuminated urban landscape. Landscape Ecology, 35, pp.189-201.

Walters, C.L., Collen, A., Lucas, T., Mroz, K., Sayer, C.A. and Jones, K.E., 2013. Challenges of using bioacoustics to globally monitor bats. Bat evolution, ecology, and conservation, pp.479-499.

Wang, J. and Bu, Y., 2022. Internet of Things‐based smart insect monitoring system using a deep neural network. IET Networks, 11(6), pp.245-256.

Whittaker, A. (2020, October 16). Ultrasonically detect bats with raspberry Pi. Raspberry Pi.
https://www.raspberrypi.com/news/ultrasonically-detect-bats-with-raspberry-pi/ 

Whytock, R.C. and Christie, J., 2017. Solo: an open source, customizable and inexpensive audio recorder for bioacoustic research. 
Methods in Ecology and Evolution, 8(3), pp.308-312.

Zeale, M.R., Stone, E.L., Zeale, E., Browne, W.J., Harris, S. and Jones, G., 2018. 
Experimentally manipulating light spectra reveals the importance of dark corridors for commuting bats. Global Change Biology, 24(12), pp.5909-5918.

References for Codes (Excluding BatDecect2/Acoupi – noted as footnotes on page 18) 

Temperature/Humidity Sensor: https://github.com/adafruit/Adafruit_CircuitPython_SHT4x

Lux Sensor: https://github.com/adafruit/Adafruit_CircuitPython_TSL2591

GPS Sensor: https://github.com/adafruit/Adafruit_CircuitPython_GPS

Automated Process: https://github.com/Unitech/pm2

Firebase API for Flutter App: https://github.com/thisbejim/Pyrebase

The following codes were used for bat call data analysis recorded only by EchoPiBox 2.0 

https://github.com/pandas-dev/pandas

https://github.com/numpy/numpy

https://github.com/plotly/plotly.py
