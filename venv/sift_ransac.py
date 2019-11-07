    
    # 读取图像
    Mat img01=imread("/home/kyaking/downloads/pic/rose_seq_auto/matches/DSC_3428.desc");
    Mat img02=imread("/home/kyaking/downloads/pic/rose_seq_auto/matches/matches.f.bin");
    imshow("original image1",img01);
    imshow("original image2",img02);

    # //SIFT特征检测
    SiftFeatureDetector detector;        //定义特点点检测器
    vector<KeyPoint> keypoint01,keypoint02;//定义两个容器存放特征点
    detector.detect(img01,keypoint01);
    detector.detect(img02,keypoint02);

    # //在两幅图中画出检测到的特征点
    Mat_out_img01;
    Mat_out_img02;
    drawKeypoints(img01,keypoint01,out_img01);
    drawKeypoints(img02,keypoint02,out_img02);
    imshow("特征点图01",out_img01);
    imshow("特征点图02",out_img02);

    # //提取特征点的特征向量（128维）
    SiftDescriptorExtractor extractor;
    Mat descriptor01,descriptor02;
    extractor.compute(img01,keypoint01,descriptor01);
    extractor.compute(img02,keypoint02,descriptor02);

    # //匹配特征点，主要计算两个特征点特征向量的欧式距离，距离小于某个阈值则认为匹配

    BruteForceMatcher<L2<float>> matcher;
    vector<DMatch> matches;
    Mat img_matches;
    matcher.match(descriptor01,descriptor02,matches);
    drawMatches(img01,keypoint01,img02,keypoint02,matches,img_matches);
    imshow("误匹配消除前",img_matches);