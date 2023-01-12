/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QVBoxLayout *verticalLayout;
    QWidget *shadowWidget;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QPushButton *btnMin;
    QPushButton *btnMax;
    QPushButton *btnClose;
    QFrame *frame;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QString::fromUtf8("Widget"));
        Widget->resize(769, 511);
        verticalLayout = new QVBoxLayout(Widget);
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(9, 9, 9, 9);
        shadowWidget = new QWidget(Widget);
        shadowWidget->setObjectName(QString::fromUtf8("shadowWidget"));
        shadowWidget->setStyleSheet(QString::fromUtf8("#shadowWidget\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}"));
        verticalLayout_2 = new QVBoxLayout(shadowWidget);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(shadowWidget);
        label->setObjectName(QString::fromUtf8("label"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        QFont font;
        font.setPointSize(16);
        label->setFont(font);
        label->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(label);

        btnMin = new QPushButton(shadowWidget);
        btnMin->setObjectName(QString::fromUtf8("btnMin"));
        btnMin->setMinimumSize(QSize(40, 40));
        btnMin->setMaximumSize(QSize(40, 40));
        btnMin->setStyleSheet(QString::fromUtf8(" QPushButton {\n"
"     border: none;\n"
" }\n"
"\n"
" QPushButton:hover\n"
"{\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
" QPushButton:pressed\n"
"{\n"
"	background-color: rgb(0, 216, 216);\n"
"}\n"
""));

        horizontalLayout->addWidget(btnMin);

        btnMax = new QPushButton(shadowWidget);
        btnMax->setObjectName(QString::fromUtf8("btnMax"));
        btnMax->setMinimumSize(QSize(40, 40));
        btnMax->setMaximumSize(QSize(40, 40));
        btnMax->setStyleSheet(QString::fromUtf8(" QPushButton {\n"
"     border: none;\n"
" }\n"
"\n"
" QPushButton:hover\n"
"{\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
" QPushButton:pressed\n"
"{\n"
"	background-color: rgb(0, 216, 216);\n"
"}\n"
""));

        horizontalLayout->addWidget(btnMax);

        btnClose = new QPushButton(shadowWidget);
        btnClose->setObjectName(QString::fromUtf8("btnClose"));
        btnClose->setMinimumSize(QSize(40, 40));
        btnClose->setMaximumSize(QSize(40, 40));
        btnClose->setStyleSheet(QString::fromUtf8(" QPushButton {\n"
"     border: none;\n"
"	background-color: rgb(255, 52, 11);\n"
"	border-top-right-radius:5px;\n"
" }\n"
"\n"
" QPushButton:hover\n"
"{\n"
"	background-color: rgb(255, 74, 58);\n"
"}\n"
" QPushButton:pressed\n"
"{\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"\n"
""));

        horizontalLayout->addWidget(btnClose);


        verticalLayout_2->addLayout(horizontalLayout);

        frame = new QFrame(shadowWidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);

        verticalLayout_2->addWidget(frame);


        verticalLayout->addWidget(shadowWidget);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QCoreApplication::translate("Widget", "Widget", nullptr));
        label->setText(QCoreApplication::translate("Widget", "Frameless Window", nullptr));
        btnMin->setText(QString());
        btnMax->setText(QString());
        btnClose->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
