#include "widget.h"
#include "ui_widget.h"
#include <QMouseEvent>
#include <QGraphicsDropShadowEffect> //窗口拖动阴影的头文件

//style sheet 帮助文档搜索查询配置样式说明

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    testfunction();

    Lession2lib lib;

    this->setWindowFlags(Qt::FramelessWindowHint);  //无边框

    QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(); //阴影边框效果类

    shadow->setBlurRadius(10);
    shadow->setColor(Qt::black);
    shadow->setOffset(0); //偏移
    this->setAttribute(Qt::WA_TranslucentBackground); //设置主窗口透明

    ui->shadowWidget->setGraphicsEffect(shadow);
//    this->setGraphicsEffect(shadow);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::mouseMoveEvent(QMouseEvent *event)
{
    QWidget::mouseMoveEvent(event);

    QPoint y =event->globalPos();

    QPoint x = y -this->z;

    this->move(x);
}

void Widget::mousePressEvent(QMouseEvent *event)
{
    QWidget::mousePressEvent(event);

    QPoint y = event ->globalPos(); //鼠标相对于桌面左上角的位置，鼠标全局位置
    QPoint x = this->geometry().topLeft(); //窗口左上角相对于桌面左上角的位置
    this->z = y-x; //z是定值
}

void Widget::mouseReleaseEvent(QMouseEvent *event)
{
    QWidget::mouseReleaseEvent(event);
    this->z = QPoint();
}


void Widget::on_btnClose_clicked()
{
    this->close();
}


void Widget::on_btnMax_clicked()
{
    if(this->isMaximized())
    {
        ui->verticalLayout->setMargin(9);
        this->showNormal();
    }
    else
    {
        ui->verticalLayout->setMargin(0);
        this->showMaximized();
    }
}


void Widget::on_btnMin_clicked()
{
    this->showMinimized();
}

