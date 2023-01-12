#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include "lession2lib.h"

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

    void mouseMoveEvent(QMouseEvent *event);
    void mousePressEvent(QMouseEvent *event);
    void mouseReleaseEvent(QMouseEvent *event);

private slots:
    void on_btnClose_clicked();

    void on_btnMax_clicked();

    void on_btnMin_clicked();

private:
    Ui::Widget *ui;
    QPoint z;
};
#endif // WIDGET_H
